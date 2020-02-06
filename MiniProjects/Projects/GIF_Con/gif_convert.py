import imageio
import os
clip = os.path.abspath('D:\Projects\Codes\Challenges\python_challenges\gif_converter\stock1.mp4')


def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat
    print(f'Converting {inputPath} to {outputPath}')
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputPath, fps=fps)
    for frames in reader:
        writer.append_data(frames)
        print(f'Frames {frames}')
    print('\n\n     CONVERTING DONE     \n\n')
    writer.close()


gifMaker(clip, '.gif')
