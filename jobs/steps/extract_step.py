def extract_from_folders(folders: str):
    urls = []
    for folder in folders:
        if 'drive.google.com' in folder:
            # yield from extract_from_google_drive(folder)
            for url in folder:
                urls.append(folder)
        else:
            raise Exception('Not supported folder')
    return []

