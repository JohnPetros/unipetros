module.exports = {
  content: [
    './src/ui/templates/**/*.html',
    './src/ui/static/src/**/*.js',
    'node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {
      colors: {
        petros: {
          50: '#efeff6',
          100: '#cfcedf',
          200: '#aeaecb',
          300: '#8d8db8',
          400: '#6d6ca5',
          500: '#53528c',
          600: '#41406c',
          700: '#2f2e4c',
          800: '#1c1b2d',
          900: '#090910',
        },
        blue: {
          50: '#def9ff',
          100: '#b6e7f8',
          200: '#8ed6f0',
          300: '#63c5e8',
          400: '#3cb5e1',
          500: '#259bc7',
          600: '#17799c',
          700: '#095670',
          800: '#003546',
          900: '#00131b',
        }
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require('tailwindcss-animated'),
  ],
}