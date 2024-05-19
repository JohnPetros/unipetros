from flask import send_file, after_this_request

from core.use_cases.admin import create_professors_csv

from infra.auth import login_checker, role_checker
from infra.utils.file import File


@login_checker
@role_checker("admin")
def get_professors_csv_view():

    csv_file = create_professors_csv.execute()
    csv_folder = csv_file["folder"]
    csv_filename = csv_file["filename"]
    csv_path = f"{csv_folder}/{csv_filename}"

    @after_this_request
    def _(response):
        File(csv_file["folder"], csv_file["filename"]).delete()

        return response

    return send_file(csv_path, as_attachment=True)
