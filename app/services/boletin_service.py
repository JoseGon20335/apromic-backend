import os
from werkzeug.utils import secure_filename

class BoletinService:
    def __init__(self, db, bucket):
        self.db = db
        self.bucket = bucket

    def upload_boletin(self, file, name_boletin):
        # Guardar archivo en Firebase Storage
        filename = secure_filename(file.filename)
        blob = self.bucket.blob(f'boletines/{filename}')
        blob.upload_from_file(file)

        # Guardar referencia en Firestore
        boletin_data = {
            'boletin_path': blob.public_url,
            'name_boletin': name_boletin
        }
        self.db.collection('boletin').add(boletin_data)

    def get_boletin(self, boletin_id):
        boletin_ref = self.db.collection('boletin').document(boletin_id)
        boletin = boletin_ref.get()
        return boletin.to_dict() if boletin.exists else None

    def delete_boletin(self, boletin_id):
        boletin_ref = self.db.collection('boletin').document(boletin_id)
        boletin = boletin_ref.get()
        if boletin.exists:
            boletin_data = boletin.to_dict()
            # Borrar archivo de Firebase Storage
            blob = self.bucket.blob(boletin_data['boletin_path'])
            blob.delete()
            # Borrar referencia en Firestore
            boletin_ref.delete()
