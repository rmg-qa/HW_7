from zipfile import ZipFile
import io
import PyPDF2
import pandas
from openpyxl import load_workbook


# Проверка на то, что путь к файлам архива существует
def test_check_path_archive(create_zip_archive):
    if create_zip_archive == 'resources\\archive.zip':
        print('Данный путь к файлам архива существует')
    else:
        print('Данный путь к файлам архива не существует')


# проверка pdf-файла
def test_check_pdf(create_zip_archive):
    with ZipFile(create_zip_archive, 'r') as zip_file:
        with zip_file.open('tmp/Dummy-PDF-3Pages.pdf') as pdf_file:
            reader = PyPDF2.PdfReader((io.BytesIO(pdf_file.read())))
            print(len(reader.pages))
            assert 'Sample T ext PDF' in reader.pages[0].extract_text()


    # проверка xlsx-файла
def test_check_xlsx(create_zip_archive):
    with ZipFile(create_zip_archive, 'r') as zip_file:
        with zip_file.open('tmp/1mb.xlsx') as xlsx_file:
            workbook = load_workbook((io.BytesIO(xlsx_file.read())))
            sheet = workbook.active
            print(sheet.cell(row=2, column=2).value)
            assert sheet.cell(row=2, column=2).value == 'rubye.bernhard@gmail.com'


    # # проверка csv-файла
def test_check_csv(create_zip_archive):
    with ZipFile(create_zip_archive, 'r') as zip_file:
        with zip_file.open('tmp/example_2.5kb.csv') as csv_file:
            reader = pandas.read_csv(csv_file)['name'].tolist()
            print(reader)
            assert 'Prof. Gerardo Deckow V' in reader
