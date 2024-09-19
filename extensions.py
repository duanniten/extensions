import csv
def main():
    extensions = loadExtensions()
    input_file = inputFile()
    getExtenion(input_file, extensions)




def getExtenion(file:str,dic:dict):
    for suffix, file_type in dic.items():
        if file.endswith(suffix):
            print(file_type[0])  # Retorna o primeiro valor da lista
            return
    print('application/octet-stream')

def inputFile():
    return input("File name: ").strip().lower()

def loadExtensions(f='extensions.csv'):
    extencions= dict()
    extencions['.aac'] = 'audio/aac'
    extencions['.abw'] = 'application/x-abiword'
    extencions['.apng'] = 'image/apng'
    extencions['.arc'] = 'application/x-freearc'
    extencions['.avif'] = 'image/avif'
    extencions['.avi'] = 'video/x-msvideo'
    extencions['.azw'] = 'application/vnd.amazon.ebook'
    extencions['.bin'] = 'application/octet-stream'
    extencions['.bmp'] = 'image/bmp'
    extencions['.bz'] = 'application/x-bzip'
    extencions['.bz2'] = 'application/x-bzip2'
    extencions['.cda'] = 'application/x-cdf'
    extencions['.csh'] = 'application/x-csh'
    extencions['.css'] = 'text/css'
    extencions['.csv'] = 'text/csv'
    extencions['.doc'] = 'application/msword'
    extencions['.docx'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    extencions['.eot'] = 'application/vnd.ms-fontobject'
    extencions['.epub'] = 'application/epub+zip'
    extencions['.gz'] = 'application/gzip'
    extencions['.gif'] = 'image/gif'
    extencions['.htm    text/html'] = ''
    extencions['.html'] = 'text/html'
    extencions['.ico'] = 'image/vnd.microsoft.icon'
    extencions['.ics'] = 'text/calendar'
    extencions['.jar'] = 'application/java-archive'
    extencions['.jpeg   image/jpeg'] = ''
    extencions['.jpg'] = 'image/jpeg'
    extencions['.js'] = 'text/javascript'
    extencions['.json'] = 'application/json'
    extencions['.jsonld'] = 'application/ld+json'
    extencions['.mid    audio/midi, audio/x-midi'] = ''
    extencions['.midi   audio/midi, audio/x-midi'] = ''
    extencions['.mjs'] = 'text/javascript'
    extencions['.mp3'] = 'audio/mpeg'
    extencions['.mp4'] = 'video/mp4'
    extencions['.mpeg'] = 'video/mpeg'
    extencions['.mpkg'] = 'application/vnd.apple.installer+xml'
    extencions['.odp'] = 'application/vnd.oasis.opendocument.presentation'
    extencions['.ods'] = 'application/vnd.oasis.opendocument.spreadsheet'
    extencions['.odt'] = 'application/vnd.oasis.opendocument.text'
    extencions['.oga'] = 'audio/ogg'
    extencions['.ogv'] = 'video/ogg'
    extencions['.ogx'] = 'application/ogg'
    extencions['.opus'] = 'audio/ogg'
    extencions['.otf'] = 'font/otf'
    extencions['.png'] = 'image/png'
    extencions['.pdf'] = 'application/pdf'
    extencions['.php'] = 'application/x-httpd-php'
    extencions['.ppt'] = 'application/vnd.ms-powerpoint'
    extencions['.pptx'] = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    extencions['.rar'] = 'application/vnd.rar'
    extencions['.rtf'] = 'application/rtf'
    extencions['.sh'] = 'application/x-sh'
    extencions['.svg'] = 'image/svg+xml'
    extencions['.tar'] = 'application/x-tar'
    extencions['.tif    image/tiff'] = ''
    extencions['.tiff   image/tiff'] = ''
    extencions['.ts'] = 'video/mp2t'
    extencions['.ttf'] = 'font/ttf'
    extencions['.txt'] = 'text/plain'
    extencions['.vsd'] = 'application/vnd.visio'
    extencions['.wav'] = 'audio/wav'
    extencions['.weba'] = 'audio/webm'
    extencions['.webm'] = 'video/webm'
    extencions['.webp'] = 'image/webp'
    extencions['.woff'] = 'font/woff'
    extencions['.woff2'] = 'font/woff2'
    extencions['.xhtml'] = 'application/xhtml+xml'
    extencions['.xls'] = 'application/vnd.ms-excel'
    extencions['.xlsx'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    extencions['.xml'] = 'application/xml'
    extencions['.xul'] = 'application/vnd.mozilla.xul+xml'
    extencions['.zip'] = 'application/zip'
    extencions['.3gp'] = 'video/3gpp; audio/3gpp '
    extencions['.3g2'] = 'video/3gpp2; audio/3gpp2'
    extencions['.7z'] = 'application/x-7z-compressed'
    return extencions

main()

