"""
Use this script to reformat wav files from IEEE-FLOAT to PCM 16
place the files in a directory with the following hierarchy:
data_directory/group/speaker/[file_id1.wav, file_id2.wav, ...,
                              speaker.trans.txt]
Note that speaker.trans.txt will need to be edited to include the transcriptions
"""
import os
import soundfile as sf
import argparse


def main(input_directory, data_directory, group, speaker, chapter):
    wav_file_count = 0
    save_path = os.path.join(data_directory, group, speaker, chapter)
    idtag = speaker+'-'+chapter
    transcript_filename = idtag + '.trans.txt'
    os.makedirs(save_path, exist_ok=True)
    outfile = open(os.path.join(save_path, transcript_filename), 'w')
    save_path = os.path.join(data_directory, group, speaker, chapter)
    for file in os.listdir(input_directory):
        if file.endswith(".wav"):
            data, samplerate = sf.read(os.path.join(input_directory,file))
            sf.write('testwavout.wav',data,samplerate)
            # save the file to its new place
            ident = idtag + '-' + '{:04d}'.format(wav_file_count)
            new_filename = ident+'.wav'
            print(ident)
            os.replace('testwavout.wav',os.path.join(save_path,new_filename))
            wav_file_count += 1
            outfile.write(ident+' \n')
    outfile.close()
	

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_directory', type=str,
                        help='Path to input directory')
    parser.add_argument('data_directory', type=str,
                        help='Path to output data directory')
    parser.add_argument('group', type=str,
                        help='group')
    parser.add_argument('speaker', type=str,
                        help='speaker number')
    parser.add_argument('chapter', type=str,
                        help='chapter number')
    args = parser.parse_args()
    main(args.input_directory, args.data_directory, args.group, args.speaker, args.chapter)
