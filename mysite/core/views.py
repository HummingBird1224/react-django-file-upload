from distutils.util import convert_path
from email.mime import image
from tkinter import Image
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os
from .forms import BookForm

from django.conf import settings

from pdf2image import convert_from_path, convert_from_bytes
from fpdf import FPDF
from pdf2docx import parse
from docx2pdf import convert
import aspose.words as aw
from PIL import Image
import cv2
from rest_framework.decorators import api_view
from rest_framework.response import Response

class Home(TemplateView):
    template_name = 'upload.html'

# def docxtopdf(input,output):
#     convert(input,output)
download_url=""
@api_view(['GET', 'POST'])
def upload(request):
    print("text!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    context = {}
    url_output={'url':''}
    if request.method == 'POST':
        
        print("text")
        uploaded_file = request.FILES['document']
        converter_type=request.POST['filetype']
        source_type=uploaded_file.name.split(".")[1]
        print(source_type)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        context['url']=context['url'].replace('%20',' ')
        url=settings.BASE_DIR
        url=url.replace( '\\','/' )
        if converter_type=='jpg' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.jpg'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.jpg','JPEG')
        if converter_type=='gif' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.gif'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.gif','JPEG')
        if converter_type=='bmp' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.bmp'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.bmp','JPEG')        
        if converter_type=='png' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.png'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.png','JPEG')
        if converter_type=='odd' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.odd'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.odd','JPEG')
        if converter_type=='ico' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.ico'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.ico','JPEG')
        if converter_type=='svg' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.svg'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.svg','JPEG')        
        if converter_type=='eps' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.eps'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.eps','JPEG')
        if converter_type=='psd' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.psd'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.psd','JPEG') 
        if converter_type=='tiff' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.tiff'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.tiff','JPEG')
        if converter_type=='webp' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.webp'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.webp','JPEG')     
        if converter_type=='tga' and source_type=='pdf':
            
            url_output['url']='/media'+'/output.tga'
            url=url+context['url']
            image=convert_from_path(url)
            for img in image:
                img.save('./media/output.tga','JPEG')                    
        
        if converter_type=='pdf'and source_type=='png':
            
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0)
            pdf.output('./media/output.pdf','F')
        if converter_type=='pdf'and source_type=='gif':
            
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0)
            pdf.output('./media/output.pdf','F')
        if converter_type=='pdf'and source_type=='jpg':
            
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0)
            pdf.output('./media/output.pdf','F')
        if converter_type=='pdf'and source_type=='bmp':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F') 
        # if converter_type=="docx" and source_type=="jpg":
        #     url_output['url']='/media'+'/sampledoc'+'/sample.docx'
        #     url=url+context['url']
        #     parse(url, url_output, start=1, end=3)
        if converter_type=='pdf'and source_type=='svg':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F')         
        if converter_type=='pdf'and source_type=='odd':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F')        
        if converter_type=='pdf'and source_type=='psd':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F')  
        if converter_type=='pdf'and source_type=='ico':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F')   
        if converter_type=='pdf'and source_type=='eps':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F') 
        if converter_type=='pdf'and source_type=='tiff':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F')     
        if converter_type=='pdf'and source_type=='webp':
            url_output['url']='/media'+'/output.pdf'
            url=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url,0,0) 
            pdf.output('./media/output.pdf','F')                                                   
        if converter_type=='pdf' and source_type=='docx':
            print("DocToPDF")
            url_output['url']='/media'+'/output.pdf'
            url_source=url+context['url']
            url_docx=url+'/media'+'/output.pdf'
            doc = aw.Document(url_source)

# Save as PDFur
            doc.save(url_docx)
        if converter_type=='pdf' and source_type=='doc':
            print("DocToPDF")
            url_output['url']='/media'+'/doctopdf'+'/output.pdf'
            url_source=url+context['url']
            url_docx=url+'/media'+'/doctopdf'+'/output.pdf'
            doc = aw.Document(url_source)

# Save as PDFur
            doc.save(url_docx)        
        if converter_type=='pdf' and source_type=='txt':
            print("DocToPDF")
            url_output['url']='/media'+'/doctopdf'+'/output.pdf'
            url_source=url+context['url']
            url_docx=url+'/media'+'/doctopdf'+'/output.pdf'
            doc = aw.Document(url_source)
            doc.save(url_docx)        
        if converter_type=='doc' and source_type=='pdf':
            url_output['url']='/media'+'/output.doc'
            url_source=url+context['url']
            url_docx=url+'/media'+'/output.doc'
            doc=aw.Document(url_source)
            doc.save(url_docx)         
          
        if converter_type=='docx' and source_type=='pdf':
            url_output['url']='/media'+'/output.docx'
            url_source=url+context['url']
            url_docx=url+'/media'+'/output.docx'
            doc=aw.Document(url_source)
            doc.save(url_docx)         
          
        if converter_type=='txt' and source_type=='pdf':
            url_output['url']='/media'+'/output.txt'
            url_source=url+context['url']
            url_docx=url+'/media'+'/output.txt'
            doc=aw.Document(url_source)
            doc.save(url_docx)
        if converter_type=='doc'and source_type=='jpg':
            
            url_output['url']='/media'+'/output.doc'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.doc'
            doc.save(url_doc)
        if converter_type=='doc'and source_type=='png':
            
            url_output['url']='/media'+'/output.doc'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.doc'
            doc.save(url_doc)
        if converter_type=='doc'and source_type=='bmp':
            
            url_output['url']='/media'+'/output.doc'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.doc'
            doc.save(url_doc)        
        if converter_type=='doc'and source_type=='gif':
            
            url_output['url']='/media'+'/output.doc'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.doc'
            doc.save(url_doc)
        if converter_type=='txt'and source_type=='jpg':
            
            url_output['url']='/media'+'/output.txt'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.txt'
            doc.save(url_doc)
        if converter_type=='txt'and source_type=='png':
            
            url_output['url']='/media'+'/output.txt'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.txt'
            doc.save(url_doc)
        if converter_type=='txt'and source_type=='bmp':
            
            url_output['url']='/media'+'/output.txt'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.txt'
            doc.save(url_doc)        
        if converter_type=='txt'and source_type=='gif':
            
            url_output['url']='/media'+'/output.txt'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.txt'
            doc.save(url_doc)
        if converter_type=='docx'and source_type=='JPG':
            
            url_output['url']='/media'+'/output.docx'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.docx'
            doc.save(url_doc)
        if converter_type=='docx'and source_type=='png':
            
            url_output['url']='/media'+'/output.docx'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.docx'
            doc.save(url_doc)
        if converter_type=='docx'and source_type=='bmp':
            
            url_output['url']='/media'+'/output.docx'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.docx'
            doc.save(url_doc)        
        if converter_type=='docx'and source_type=='gif':
            
            url_output['url']='/media'+'/output.docx'
            url_source=url+context['url']
            pdf=FPDF()
            pdf.add_page()
            pdf.image(url_source,0,0)
            pdf.output('./media/output.pdf','F')
            doc=aw.Document(url+'/media'+'/output.pdf')
            url_doc=url+'/media'+'/output.docx'
            doc.save(url_doc)        
        
        if converter_type=='jpg' and source_type=='png':
            url_output['url']='/media'+'/output.jpg'
            url_converter=url+'/media'+'/output.jpg'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        if converter_type=='png' and source_type=='jpg':
            url_output['url']='/media'+'/output.png'
            url_converter=url+'/media'+'/output.png'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_PNG_COMPRESSION), 100])   
        if converter_type=='webp' and source_type=='png':
            url_output['url']='/media'+'/output.webp'
            url_converter=url+'/media'+'/output.webp'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_WEBP_QUALITY), 100])   
        if converter_type=='png' and source_type=='webp':
            url_output['url']='/media'+'/output.png'
            url_converter=url+'/media'+'/output.png'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_PNG_COMPRESSION), 100])                            
        if converter_type=='webp' and source_type=='jpg':
            url_output['url']='/media'+'/output.webp'
            url_converter=url+'/media'+'/output.webp'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_WEBP_QUALITY), 100])   
        if converter_type=='jpg' and source_type=='webp':
            url_output['url']='/media'+'/output.jpg'
            url_converter=url+'/media'+'/output.jpg'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
        if converter_type=='webp' and source_type=='png':
            url_output['url']='/media'+'/output.webp'
            url_converter=url+'/media'+'/output.webp'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_WEBP_QUALITY), 100])   
        if converter_type=='png' and source_type=='webp':
            url_output['url']='/media'+'/output.png'
            url_converter=url+'/media'+'/output.png'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_PNG_COMPRESSION), 100])   
        if converter_type=='tiff' and source_type=='png':
            url_output['url']='/media'+'/output.tiff'
            url_converter=url+'/media'+'/output.tiff'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_TIFF_COMPRESSION), 100])   
        if converter_type=='png' and source_type=='tiff':
            url_output['url']='/media'+'/output.png'
            url_converter=url+'/media'+'/output.png'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_PNG_COMPRESSION), 100])          
        if converter_type=='tiff' and source_type=='jpg':
            url_output['url']='/media'+'/output.tiff'
            url_converter=url+'/media'+'/output.tiff'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_TIFF_COMPRESSION), 100])   
        if converter_type=='jpg' and source_type=='tiff':
            url_output['url']='/media'+'/output.jpg'
            url_converter=url+'/media'+'/output.jpg'
            url_source=url+context['url']
            img_png = cv2.imread(url_source)
  
#The image object is used to save the image in jpg format
            cv2.imwrite(url_converter, img_png, [int(cv2.IMWRITE_JPEG_QUALITY), 100])   
                              
    return Response(url_output)


# @api_view(['GET', 'POST'])
# def download_file(request):
#     if request=='POST':
#         print("download!!!!!!!!!!!!!!!!!!!!!!!")
#         return Response("okkkkk")
