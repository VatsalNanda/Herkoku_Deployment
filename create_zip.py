import zipfile
import os
zip_file=zipfile.ZipFile('mashup.zip','w')
zip_file.write('merged_final.mp3', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()
