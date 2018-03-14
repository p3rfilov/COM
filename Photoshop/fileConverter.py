from comtypes.client import CreateObject
import os

class Converter():
    '''
    Convert files to different formats using Photoshop
    
    Class usage:
        Converter(['png', 'file1.psd', 'file2.psd', 'file3.psd'])
        
    Cmd execution:
        fileConverter.py "png" "file1.psd" "file2.psd" "file3.psd"
    '''
    def __init__(self, arguments):
        self.ps = CreateObject('Photoshop.Application')
        self.ps.Preferences.RulerUnits = 1
        self.format = ''
        self.files = []
        
        if arguments:
            self.format = arguments[0]
            self.files = arguments[1:]
        else:
            print('No arguments have been passed!')
        
        if self.format.lower() == 'png':
            self.convertToPNG()
        
        self.quit()
    
    def convertToPNG(self):
        for file in self.files:
            self.ps.Application.Open(file)
            outFile = os.path.splitext(file)[0] + '.png'
            
            options = CreateObject('Photoshop.PNGSaveOptions')
            options.Compression = 1
            options.Interlaced = False
            saveAsCopy = True
            
            self.ps.ActiveDocument.SaveAs(outFile, options, saveAsCopy)
            self.ps.ActiveDocument.Close()
    
    def quit(self):
        #Close Photoshop if no documents are open
        if not self.ps.Documents.Count: self.ps.Application.Quit()
        
if __name__ == '__main__':
    import sys
    
    Converter(sys.argv[1:])
    