import streamlit as st
import yaml
import io
from PIL import Image
from predict import load_model,get_prediction 
from confirm_button_hack import cache_on_button_press
st.set_page_config(layout ='wide')
def main():
    st.title('Mask Classification model')
    with open('config.yaml') as f:
        config = yaml.load(f, Loader = yaml.FullLoader)
    model = load_model()
    model.eval() 
    uploader = st.file_uploader("choose an Image",type = ['jpg','png','jpeg']) 
    if uploader:
        # TODO : image view
        image_bytes = uploader.getvalue()
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image,caption = 'uploaded image ')
        loading = st.text('Classifying... ')
        _, y_hat = get_prediction(model,image_bytes)
        label = config['classes'][y_hat.item()]
        loading.text(
            f'''predict is done...
            label is {label}
            '''
        )
root_password = 'password'
password = st.text_input('password',type = 'password')

@cache_on_button_press('Authenticate')
def authenticate(password):
    st.write(type(password))
    return password == root_password

if authenticate(password):
    st.success('인증완료!')
    main()

else:
    st.error('password worng')