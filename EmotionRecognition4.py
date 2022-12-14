#!/usr/bin/env python

"""
======================================================
Emotion recognition using SVMs (Scikit-learn & OpenCV)
======================================================

Author: Athira Nirmal:Aishwarya V Nair:Juhi Fathima
        S8 CS1
        LBS Institue of Technology,Poojapura.

Dependencies: Python 2.7, Scikit-Learn, OpenCV 3.0.0,
              Numpy, Scipy, Matplotlib, Tkinter

The dataset used in this example is Olivetti Faces:
 http://cs.nyu.edu/~roweis/data/olivettifaces.mat

"""
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import json
import subprocess
from sklearn import datasets
import FileDialog   # Needed for Pyinstaller
from sklearn.svm import SVC
from sklearn.cross_validation  import train_test_split
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem
from sklearn import metrics
import cv2
import numpy as np
from scipy.ndimage import zoom
from sklearn import datasets
import sys, os, subprocess
import pandas, random

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

print(__doc__)



faces = datasets.fetch_olivetti_faces()

#music
actions = {}
df = pandas.read_excel("EmotionLinks.xlsx") #open Excel file
actions["happy"] = [x for x in df.happy.dropna()]
actions["sad"] = [x for x in df.sad.dropna()]


# ==========================================================================
# Traverses through the dataset by incrementing index & records the result
# ==========================================================================
class Trainer:
    def __init__(self):
        self.results = {}
        self.imgs = faces.images
        self.index = 0

    def reset(self):
        print "============================================"
        print "Resetting Dataset & Previous Results.. Done!"
        print "============================================"
        self.results = {}
        self.imgs = faces.images
        self.index = 0

    def increment_face(self):
        if self.index + 1 >= len(self.imgs):
            return self.index
        else:
            while str(self.index) in self.results:
                # print self.index
                self.index += 1
            return self.index

    def record_result(self, smile=True):
        print "Image", self.index + 1, ":", "Happy" if smile is True else "Sad"
        self.results[str(self.index)] = smile


# ===================================
# Callback function for the buttons
# ===================================
## smileCallback()              : Gets called when "Happy" Button is pressed
## noSmileCallback()            : Gets called when "Sad" Button is pressed
## updateImageCount()           : Displays the number of images processed
## displayFace()                : Gets called internally by either of the button presses
## displayBarGraph(isBarGraph)  : computes the bar graph after classification is completed 100%
## _begin()                     : Resets the Dataset & Starts from the beginning
## _quit()                      : Quits the Application
## printAndSaveResult()         : Save and print the classification result
## loadResult()                 : Loading the previously stored classification result
## run_once(m)                  : Decorator to allow functions to run only once

def run_once(m):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return m(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

def smileCallback():
    trainer.record_result(smile=True)
    trainer.increment_face()
    displayFace(trainer.imgs[trainer.index])
    updateImageCount(happyCount=True, sadCount= False)


def noSmileCallback():
    trainer.record_result(smile=False)
    trainer.increment_face()
    displayFace(trainer.imgs[trainer.index])
    updateImageCount(happyCount=False, sadCount=True)


def updateImageCount(happyCount, sadCount):
    global HCount, SCount, imageCountString, countString   # Updating only when called by smileCallback/noSmileCallback
    if happyCount is True and HCount < 400:
        HCount += 1
    if sadCount is True and SCount < 400:
        SCount += 1
    if HCount == 400 or SCount == 400:
        HCount = 0
        SCount = 0
    # --- Updating Labels
    # -- Main Count
    imageCountPercentage = str(float((trainer.index + 1) * 0.25)) \
        if trainer.index+1 < len(faces.images) else "Classification DONE! 100"
    imageCountString = "Image Index: " + str(trainer.index+1) + "/400   " + "[" + imageCountPercentage + " %]"
    labelVar.set(imageCountString)           # Updating the Label (ImageCount)
    # -- Individual Counts
    countString = "(Happy: " + str(HCount) + "   " + "Sad: " + str(SCount) + ")\n"
    countVar.set(countString)


@run_once
def displayBarGraph(isBarGraph):
    ax[1].axis(isBarGraph)
    n_groups = 1                    # Data to plot
    Happy, Sad = (sum([trainer.results[x] == True for x in trainer.results]),
               sum([trainer.results[x] == False for x in trainer.results]))
    index = np.arange(n_groups)     # Create Plot
    bar_width = 0.5
    opacity = 0.75
    ax[1].bar(index, Happy, bar_width, alpha=opacity, color='b', label='Happy')
    ax[1].bar(index + bar_width, Sad, bar_width, alpha=opacity, color='g', label='Sad')
    ax[1].set_ylim(0, max(Happy, Sad)+10)
    ax[1].set_xlabel('Expression')
    ax[1].set_ylabel('Number of Images')
    ax[1].set_title('Training Data Classification')
    ax[1].legend()


@run_once
def printAndSaveResult():
    print trainer.results                       # Prints the results
    with open("../results/results.xml", 'w') as output:
        json.dump(trainer.results, output)        # Saving The Result

@run_once
def loadResult():
    results = json.load(open("../results/results.xml"))
    trainer.results = results


def displayFace(face):
    ax[0].imshow(face, cmap='gray')
    isBarGraph = 'on' if trainer.index+1 == len(faces.images) else 'off'      # Switching Bar Graph ON
    if isBarGraph is 'on':
        displayBarGraph(isBarGraph)
        printAndSaveResult()
    # f.tight_layout()
    canvas.draw()

#music
def open_stuff(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])    

def _opencv():
    print "\n\n Please Wait. . . ."
    print "\n\n Please Wait . . . . .\n\n"

    faces = datasets.fetch_olivetti_faces()

# ==========================================================================
# Traverses through the dataset by incrementing index & records the result
# ==========================================================================
    class Trainer:
        def __init__(self):
            self.results = {}
            self.imgs = faces.images
            self.index = 0

        def reset(self):
            print "============================================"
            print "Resetting Dataset & Previous Results.. Done!"
            print "============================================"
            self.results = {}
            self.imgs = faces.images
            self.index = 0

        def increment_face(self):
            if self.index + 1 >= len(self.imgs):
                return self.index
            else:
                while str(self.index) in self.results:
                    # print self.index
                    self.index += 1
                return self.index

        def record_result(self, smile=True):
            print "Image", self.index + 1, ":", "Happy" if smile is True else "Sad"
            self.results[str(self.index)] = smile


    # Trained classifier's performance evaluation
    def evaluate_cross_validation(clf, X, y, K):
        # create a k-fold cross validation iterator
        cv = KFold(len(y), K, shuffle=True, random_state=0)
        # by default the score used is the one returned by score method of the estimator (accuracy)
        scores = cross_val_score(clf, X, y, cv=cv)
        print "Scores: ", (scores)
        print ("Mean score: {0:.3f} (+/-{1:.3f})".format(np.mean(scores), sem(scores)))


    # Confusion Matrix and Results
    def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
        clf.fit(X_train, y_train)
        print ("Accuracy on training set:")
        print (clf.score(X_train, y_train))
        print ("Accuracy on testing set:")
        print (clf.score(X_test, y_test))
        y_pred = clf.predict(X_test)
        print ("Classification Report:")
        print (metrics.classification_report(y_test, y_pred))
        print ("Confusion Matrix:")
        print (metrics.confusion_matrix(y_test, y_pred))


# ===============================================================================
# from FaceDetectPredict.py
# ===============================================================================

    def detectFaces(frame):
        cascPath = "../data/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected_faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
        return gray, detected_faces
        


    def extract_face_features(gray, detected_face, offset_coefficients):
        (x, y, w, h) = detected_face
        horizontal_offset = int(offset_coefficients[0] * w)
        vertical_offset = int(offset_coefficients[1] * h)
        extracted_face = gray[y + vertical_offset:y + h,
                         x + horizontal_offset:x - horizontal_offset + w]
        new_extracted_face = zoom(extracted_face, (64. / extracted_face.shape[0],
                                                   64. / extracted_face.shape[1]))
        new_extracted_face = new_extracted_face.astype(np.float32)
        new_extracted_face /= float(new_extracted_face.max())
        return new_extracted_face


    def predict_face_is_smiling(extracted_face):
        return True if svc_1.predict(extracted_face.reshape(1, -1)) else False

    gray1, face1 = detectFaces(cv2.imread("../data/Test3.jpg"))
    gray2, face2 = detectFaces(cv2.imread("../data/Test2.jpg"))


    def test_recognition(c1, c2):
        extracted_face1 = extract_face_features(gray1, face1[0], (c1, c2))
        print(predict_face_is_smiling(extracted_face1))
        extracted_face2 = extract_face_features(gray2, face2[0], (c1, c2))
        print(predict_face_is_smiling(extracted_face2))
        cv2.imshow('gray1', extracted_face1)
        cv2.imshow('gray2', extracted_face2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # test_recognition(0.3, 0.05)

# ------------------- LIVE FACE RECOGNITION -----------------------------------


    if __name__ == "__main__":

        svc_1 = SVC(kernel='linear')  # Initializing Classifier

        trainer = Trainer()
        results = json.load(open("../results/results.xml"))  # Loading the classification result
        trainer.results = results

        indices = [int(i) for i in trainer.results]  # Building the dataset now
        data = faces.data[indices, :]  # Image Data

        target = [trainer.results[i] for i in trainer.results]  # Target Vector
        target = np.array(target).astype(np.int32)

        # Train the classifier using 5 fold cross validation
        X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.25, random_state=0)

        # Trained classifier's performance evaluation
        evaluate_cross_validation(svc_1, X_train, y_train, 5)

        # Confusion Matrix and Results
        train_and_evaluate(svc_1, X_train, X_test, y_train, y_test)

        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            # detect faces
            gray, detected_faces = detectFaces(frame)

            face_index = 0

            cv2.putText(frame, "Press Esc to QUIT", (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)

            # predict output
            for face in detected_faces:
                (x, y, w, h) = face
                if w > 100:
                    # draw rectangle around face
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                    # extract features
                    extracted_face = extract_face_features(gray, face, (0.3, 0.05)) #(0.075, 0.05)

                    # predict smile
                    prediction_result = predict_face_is_smiling(extracted_face)

                    # draw extracted face in the top right corner
                    frame[face_index * 64: (face_index + 1) * 64, -65:-1, :] = cv2.cvtColor(extracted_face * 255, cv2.COLOR_GRAY2RGB)                

                    # annotate main image with a label
                    if prediction_result is True:
                        cv2.putText(frame, "SMILING",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, 155, 5)
                        actionlist = [x for x in actions["happy"]]#<----- get list of actions/files for detected emotion
                        random.shuffle(actionlist) #<----- Randomly shuffle the list
                        open_stuff(actionlist[0]) #<----- Open the first entry in the list
                        video_capture.release()
                    else:
                        cv2.putText(frame, "Not Smiling",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, 155, 5)
                        actionlist = [x for x in actions["sad"]]#<----- get list of actions/files for detected emotion
                        random.shuffle(actionlist) #<----- Randomly shuffle the list
                        open_stuff(actionlist[0]) #<----- Open the first entry in the list
                        video_capture.release()

                    # increment counter
                    face_index += 1

            # Display the resulting frame
            cv2.imshow('Video', frame)
            if cv2.waitKey(10) & 0xFF == 27:
                break

        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

    #opencvProcess = subprocess.Popen("Train_Classifier_and_Test_Video_Feed.py", close_fds=True, shell=True)
    # os.system('"Train Classifier.exe"')
    # opencvProcess.communicate()


def _begin():
    trainer.reset()
    global HCount, SCount
    HCount = 0
    SCount = 0
    updateImageCount(happyCount=False, sadCount=False)
    displayFace(trainer.imgs[trainer.index])


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


if __name__ == "__main__":
    # Embedding things in a tkinter plot & Starting tkinter plot
    matplotlib.use('TkAgg')
    root = Tk.Tk()
    root.wm_title("Emotion Recognition Using Scikit-Learn & OpenCV")

    # =======================================
    # Class Instances & Starting the Plot
    # =======================================
    trainer = Trainer()

    # Creating the figure to be embedded into the tkinter plot
    f, ax = plt.subplots(1, 2)
    ax[0].imshow(faces.images[0], cmap='gray')
    ax[1].axis('off')  # Initially keeping the Bar graph OFF

    # ax tk.DrawingArea
    # Embedding the Matplotlib figure 'f' into Tkinter canvas
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    print "Keys in the Dataset: ", faces.keys()
    print "Total Images in Olivetti Dataset:", len(faces.images)

    # Declaring Button & Label Instances
    # =======================================
    smileButton = Tk.Button(master=root, text='Smiling', command=smileCallback)
    smileButton.pack(side=Tk.LEFT)

    noSmileButton = Tk.Button(master=root, text='Not Smiling', command=noSmileCallback)
    noSmileButton.pack(side=Tk.RIGHT)

    labelVar = Tk.StringVar() 
    label = Tk.Label(master=root, textvariable=labelVar)
    imageCountString = "Image Index: 0/400   [0 %]"     # Initial print
    labelVar.set(imageCountString)
    label.pack(side=Tk.TOP)

    countVar = Tk.StringVar()
    HCount = 0
    SCount = 0
    countLabel = Tk.Label(master=root, textvariable=countVar)
    countString = "(Happy: 0   Sad: 0)\n"     # Initial print
    countVar.set(countString)
    countLabel.pack(side=Tk.TOP)

    opencvButton = Tk.Button(master=root, text='Next', command=_opencv)
    opencvButton.pack(side=Tk.TOP)

    resetButton = Tk.Button(master=root, text='Reset', command=_begin)
    resetButton.pack(side=Tk.TOP)

    quitButton = Tk.Button(master=root, text='Quit Application', command=_quit)
    quitButton.pack(side=Tk.TOP)

    authorVar = Tk.StringVar()
    authorLabel = Tk.Label(master=root, textvariable=authorVar)

    authorLabel.pack(side=Tk.BOTTOM)

    root.iconbitmap(r'..\icon\happy-sad.ico')
    Tk.mainloop()                               # Starts mainloop required by Tk
