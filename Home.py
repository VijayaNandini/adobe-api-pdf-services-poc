import streamlit as st
import os
import shutil
# import io
# from docx import Document
from pdf_processor import pdf_processor


input_dir = 'data'

st.set_page_config(
    page_title='Adobe PDF Services API PoC',
    page_icon='logo.png',
    layout='wide',
    initial_sidebar_state='collapsed'
)

st.markdown('''
            <style>
                .block-container{
                    padding-top: 25px;
                }
            </style>
            ''',
            unsafe_allow_html=True)

st.title("Adobe PDF Services API PoC")

def upload_input_doc():
    print("Inside upload_input_doc function")
    if st.session_state.uploaded_file is not None:
        filename = st.session_state.uploaded_file.name
        # filepath = os.path.join(input_dir,filename)
        filepath = input_dir + '/' + filename
        with open(filepath, 'wb') as f:
            f.write(st.session_state.uploaded_file.getbuffer())
        st.session_state.is_req_received = True
        st.session_state.filename = filepath

def refresh():
    print("Inside refresh function")
    st.session_state.is_req_received = False
    st.session_state.uploaded_file.name = None
    st.session_state.output_file = None

def clean_data():
    if os.path.exists(input_dir):
        for file_name in os.listdir(input_dir):
            file_path = os.path.join(input_dir, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason {e}')
    else:
        os.mkdir(input_dir)

st.info('**This app is using Adobe PDF Services APIs: Split PDF, OCR PDF, and Combine PDF.**')
st.info('**After processing, the PDF may be fully editable and searchable.**')

col1, col2, col3 = st.columns(3)


# if not os.path.exists(input_dir):
#     os.mkdir(input_dir)


if 'is_req_received' not in st.session_state:
    st.session_state['is_req_received'] = False
    st.session_state['output_file'] = None
    clean_data()

c31, c32 = col3.columns([75,25])

# col2.toggle(
#     '**Generate Output to Word document**',
# )

st.file_uploader(
    "Choose a file",
    type=['pdf'],
    key='uploaded_file',
    accept_multiple_files=False,
    on_change=upload_input_doc
)

if st.session_state.is_req_received:
    print("Request is received to process pdf.")
    with st.spinner('Processing PDF..'):
        output_filepath = pdf_processor(st.session_state.filename)
        st.session_state.output_file = str(output_filepath)


if st.session_state.output_file is not None:
    print("Trying to produce output file.")
    # document = Document(st.session_state.output_file)
    # docx_buffer = io.BytesIO()
    # document.save(docx_buffer)
    # docx_buffer.seek(0)
    output_filename = st.session_state.output_file.split('/')[-1]
    with open(st.session_state.output_file, "rb") as pdf_file:
        pdf_data = pdf_file.read()

    col2.download_button(
        label='**Download PDF generated**',
        data=pdf_data,
        file_name=output_filename,
        type='primary',
        mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    st.session_state.is_req_received = False

    c32.button(
        'Refresh',
        type='primary',
        on_click=refresh,
        help='Click here to refresh app.'
    )
#

