'''
Created on Feb 2, 2018

@author: Danny Le
'''
import soundcloud

class test:
    
    def __init__(self):
        self.client = soundcloud.Client(client_id="MgT8dvRJVcFR9fI5Szar82usLfSQdg3n")
        self.buffer = ""

    def create_trackURL(self,track_list):
        track_url = []
        track = ""
        for i in track_list:  
            track = self.client.get('/tracks/'+i.strip())
            track_url.append(track)
        return track_url
    
        
    def read_file_create_list(self):
        track_list = []
        with open('track_ids.txt', 'r') as myFile:
            data = myFile.readlines() #.replace('\n', " ")
            for i in data:
                track_list.append(i)
        return track_list


    def id_to_html(self,track_id):
        html_list = []
        for i in track_id:
            #print(str(i.strip()))
            track = self.client.get('/tracks/'+str(i.strip()))
            track_url = track.permalink_url
        
            embeded_info = self.client.get('/oembed', url = track_url)
            html_list.append(embeded_info.obj['html'])
            
        return html_list
            
    def html_to_file(self,widget_list):
        filename = "widget_html.html"
        file = open(filename, "w")
        for i in widget_list:
            #print(str(i))
            file.write(str(i))

        

def main():
    sound_info = test()
    track_list = sound_info.read_file_create_list()
    html_list = sound_info.id_to_html(track_list)
    sound_info.html_to_file(html_list)
    
    
    #track_url = sound_info.create_trackURL(track_list)
    #sound_info.embed_widget(track_url)
    
    
if __name__ == "__main__":main()