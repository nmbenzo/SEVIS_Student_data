from __future__ import print_function
import io
from googleapiclient import discovery
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.http import MediaIoBaseDownload
from Handlers.file_imports import file_id, td_id, SCOPES, Excel, file_name


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    meta = service.files().get(fileId=file_id, fields="*",
                               supportsTeamDrives=True).execute()

    print(meta)


def download_file(file_id, mimeType, file_name):
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=50, supportsTeamDrives=True, includeTeamDriveItems=True,
        corpora='teamDrive', teamDriveId=td_id,
        fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')

    if 'google-apps' in mimeType:
        return

    data = service.files().export_media(fileId=file_id, mimeType=Excel)
    fh = io.FileIO(file_name, 'wb')
    downloader = MediaIoBaseDownload(fh, data)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download: {}".format(int(status.progress() * 100)))


if __name__ == '__main__':
    main()
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)

    drive_service = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    files = drive_service.files().list(pageSize=50, supportsTeamDrives=True, includeTeamDriveItems=True,
        corpora='teamDrive', teamDriveId=td_id,
        fields="nextPageToken, files(id, name)").execute()
    for f in files['files']:
        if f['id'] == file_id:
            print(f['name'], f['id'])
            download_file(file_id, Excel, file_name)