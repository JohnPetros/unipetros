from typing import Dict, List

from pandas import DataFrame, read_excel, read_csv


class DataAnalyserProvider:
    data: DataFrame | None

    def __init__(self) -> None:
        self.data = None

    def analyse(self, data) -> None:
        self.data = data

    def read_excel(self) -> None:
        if self.__has_dataframe():
            self.data = read_excel(self.data)

    def read_csv(self) -> None:
        if self.__has_dataframe():
            self.data = read_csv(self.data)

    def convert_to_list_of_records(self) -> List[Dict] | None:
        if self.__has_dataframe():
            return self.data.to_dict("records")

        return None

    def __has_dataframe(self) -> bool:
        return self.data is not None


#  {'Nome': ['Rodrigo Branas', 'Ana Maria', 'Carlos Eduardo', 'Maria Fernanda', 'João Silva', 'Mariana Santos', 'Pedro Almeida', 'Juliana Oliveira'], 'E-mail': ['rodrigo@unipetros.com', 'anamaria@example.com', 'carlos@email.com', 'maria@email.com', 'joao@email.com', 'mariana@email.com', 'pedro@email.com', 'juliana@email.com'], 'Telefone': [12988815499, 987654321, 987654321, 987654321, 987654321, 987654321, 987654321, 987654321], 'Data de nascimento': [Timestamp('1990-12-12 00:00:00'), Timestamp('1985-06-05 00:00:00'), Timestamp('1992-06-15 00:00:00'), Timestamp('1993-07-20 00:00:00'), Timestamp('1995-10-10 00:00:00'), Timestamp('1998-03-25 00:00:00'), Timestamp('1990-09-03 00:00:00'), Timestamp('1991-11-18 00:00:00')], 'Gender': ['masculino', 'feminino', 'masculino', 'feminino', 'masculino', 'feminino', 'masculino', 'feminino'], 'Disciplinas': ['biologia,matematica', 'português,história', 'física,química', 'literatura,arte', 'geografia,inglês', 'química,biologia', 'matemática,física', 'inglês,história']}

#  [
#    {
#      'Nome': 'Rodrigo Branas',
#      'E-mail': 'rodrigo@unipetros.com',
#      'Telefone': 12988815499,
#      'Data de nascimento': Timestamp('1992-06-15 00:00:00')
#    }
#  ]
