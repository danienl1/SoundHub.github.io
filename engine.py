'''
Created on Feb 2, 2018

@author: Danny Le
'''

import soundcloud
import soundhub
import webbrowser

class Engine:
    
    def __init__(self):
        self.client = soundcloud.Client(client_id="MgT8dvRJVcFR9fI5Szar82usLfSQdg3n")
        self.data = []
    
    def read_file_create_list(self):
        track_list = []
        with open('track_ids.txt', 'r') as myFile:
            data = myFile.readlines() 
            for i in data:
                track_list.append(i)
        return track_list


    def id_list_to_html_list(self,track_id):
        html_list = []
        for i in track_id:
            track = self.client.get('/tracks/'+str(i).strip())
            track_url = track.permalink_url
        
            embeded_info = self.client.get('/oembed', url = track_url)
            html_list.append(embeded_info.obj['html'])
            
        return html_list
            
    def create_file_from_html_list(self,widget_list,filename,imagename):
        file = open(filename, "w")

        # write image header here
        file.write('<header><img src = "'+imagename+'"></header>')
        
        for i in widget_list:
            file.write(str(i))
            file.write('\n')
            # write: LIKED BY here 

    def open_html_file(self, filename):
        webbrowser.open_new_tab(filename);
  
    
if __name__ == '__main__':

    ID = soundhub.id_from_input()
    track_dict = soundhub.generate_track_dict(ID)
    track_list = soundhub.generate_sorted_match_list(track_dict)
    soundhub.print_list(track_list)

    new_list = []
    for item in track_list:
        new_list.append(item[0])

    sh = Engine()
    html_list = sh.id_list_to_html_list(new_list)

    filename = "result.html"
    imagename = "logo.png"
    sh.create_file_from_html_list(html_list,filename,imagename)
    sh.open_html_file(filename)
