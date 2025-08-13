from FlaskExercise import app, db
from flask import flash
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import uuid

def get_blob_service():
    """
    Create a BlobServiceClient dynamically using the latest app.config values.
    This ensures compatibility if app.config changes after the module is imported.
    """
    storage_url = f"https://{app.config['BLOB_ACCOUNT']}.blob.core.windows.net/"
    return BlobServiceClient(account_url=storage_url, credential=app.config['BLOB_STORAGE_KEY'])

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    scientific_name = db.Column(db.String(75))
    description = db.Column(db.String(800))
    image_path = db.Column(db.String(100))

    def __repr__(self):
        # ✅ Python 3.12 safe — f-string formatting
        return f"<Animal {self.name}>"

    def save_changes(self, file):
        if file:
            filename = secure_filename(file.filename)
            file_extension = filename.rsplit('.', 1)[-1]
            random_filename = f"{uuid.uuid4()}.{file_extension}"
            filename = random_filename

            try:
                blob_service = get_blob_service()
                blob_client = blob_service.get_blob_client(container=app.config['BLOB_CONTAINER'], blob=filename)
                blob_client.upload_blob(file, overwrite=True)

                # ✅ Delete old image if replacing
                if self.image_path:
                    old_blob_client = blob_service.get_blob_client(
                        container=app.config['BLOB_CONTAINER'],
                        blob=self.image_path
                    )
                    old_blob_client.delete_blob()

            except Exception as err:
                flash(str(err))

            self.image_path = filename

        db.session.commit()
