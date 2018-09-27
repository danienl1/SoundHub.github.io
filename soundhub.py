from operator import itemgetter
import sys
import soundcloud


client = soundcloud.Client(client_id="MgT8dvRJVcFR9fI5Szar82usLfSQdg3n")
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def id_from_input():
    return str(username_to_id(input("enter soundcloud username: ")))
    
def username_to_id(username):
    user = client.get('/resolve', url='http://soundcloud.com/'+username)
    return user.id

def id_to_username(ID):
    user = client.get('/users/'+ID)
    return user.username    

def add_song_to_dict(track_dict, track, liked_by):
    title = track.title.translate(non_bmp_map)
    print(title)
    
    if track.id not in track_dict.keys():
        track_dict[track.id] = [1,[liked_by]]
    else:
        track_dict[track.id][0] = track_dict[track.id][0] + 1
        track_dict[track.id][1].append(liked_by)
                
def generate_track_dict(ID):
    track_dict = dict()
    followings = client.get('/users/'+ID+'/followings').obj["collection"]
    
    for user in followings:
        user_id = str(user['id'])
        user_name = str(user['username'])
        tracks = client.get('/users/'+user_id+'/favorites', limit=50)

        for track in tracks:
            add_song_to_dict(track_dict, track, user_name)
    return track_dict; 

def generate_sorted_match_list(track_dict):
    track_list = []
    for key, value in track_dict.items():
        if value[0] > 1: track_list.append( (key, value[0], value[1]) )

    track_list.sort(key=itemgetter(1), reverse=True) 
    return track_list

def print_list(track_list):
    for item in track_list:
        print(item)

################ test functions 
                
def print_song_title(id):
    track = client.get('/tracks/'+str(id))
    print("TITLE:", track.title)

################ main 

if __name__ == '__main__':
    
    ID = id_from_input()
    track_dict = generate_track_dict(ID)

    track_list = generate_sorted_match_list(track_dict) 
    print_list(track_list)

