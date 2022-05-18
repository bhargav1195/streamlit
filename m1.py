import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import pyvista
from pyvista import examples

st.title('Project: Wind around the buildings')

def ShowModel1():
    ImagePath1 = Image.open('./example_project/Model.jpg')
    st.image(ImagePath1, caption='CFD Model')

def ShowModel2():
    ImagePath2 = Image.open('./example_project/velocity_Contour_Image.jpg')
    st.image(ImagePath2, caption='velocity contour')

def ShowModel3():
    ImagePath3 = Image.open('./example_project/velocity_streamline.jpg')
    st.image(ImagePath3, caption='velocity streamline')

def LoadContour():
    mesh = examples.load_uniform()
    pl = pyvista.Plotter(shape=(1,2))
    _ = pl.add_mesh(mesh, scalars='Spatial Point Data', show_edges=True)
    pl.subplot(0,1)
    _ = pl.add_mesh(mesh, scalars='Spatial Cell Data', show_edges=True)
    pl.export_html('pyvista.html')  # doctest:+SKIP

    HtmlFile = open("pyvista.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 500,width=500)

# Using "with" notation
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Model Setup'):
        ShowModel1()

with col2:
    if st.button('Post-processing'):
        ShowModel2()

with col3:
    if st.button('Report'):
        LoadContour()
    

        

