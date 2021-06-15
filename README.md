# PDF_convert_image

## What is this?

It's a little application for me to convert the PDF i need into jpg files.

When it runs the .exe file, it will search the file which ends with .pdf in the folder it belongs to.

After that, it will transform it into jpg through each page in the file, and save it in the folder named as the file name, ex: _C:/Desktop/test/example_1.jpg_ .

Last, it will print how many PDF files exists in this folder and how many jpg files have been created.

_The jpg file will be named as the name of the PDF file with the page number, such as example_1.jpg, example_2.jpg._

## Module shoud be install
* pdf2image
```python
pip install pdf2image
```
* Poppler

```
Down load from [here](http://blog.alivate.com.au/poppler-windows/).

Unzip it to C:/Program Files.

Set __C:\Program Files\poppler-0.68.0\bin__ to your system PATH.
```

## How to use it?

Copy the .exe files to the folder where the PDF you want to transform is.
