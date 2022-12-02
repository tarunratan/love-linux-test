import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage 
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from PIL import Image, ImageOps
bucketName=('bucketname')
# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

#create a bucket object to get bucket details 
bucket = client.get_bucket(bucketName)
file = st.file_uploader("Upload An file")
def main():
  if file is not None:
    file_details = {"FileName":file.name,"FileType":file.type}
    st.write(file_details)
    with open(os.path.join(file.name),"wb") as f: 
      f.write(file.getbuffer())         
      st.success("Saved File")
      st.write ("Youre uploading to bucket",bucketName)
      object_name_in_gcs_bucket = bucket.blob(""+file.name)
      object_name_in_gcs_bucket.upload_from_filename(file.name)
      st.write("Upload file to GoogleCloud path https://storage.googleapis.com/"+bucketName+path+file.name)
      
# def upload():
#                 object_name_in_gcs_bucket = bucket.blob("survey_apks/test/",file.name)
#                 # print ("path is"+ cwd + file.name)
#                 object_name_in_gcs_bucket.upload_from_filename("tempDir",file.name)
#                 file_name = os.path.join(file_dir, file.name)
#                 read_file(file_name)
#                 st.write (file_name)
#              st.session_state["upload_state"] = "Saved successfully!"
# st.write ("Youre uploading to bucket",bucketName)
# st.button("Upload file to GoogleCloud", on_click=upload)
if __name__ == "__main__":
    main()   
