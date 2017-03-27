#!/usr/bin/env python

import grabber
import numpy as np
import timeit
import time
import matplotlib.pyplot as plt
import scipy.signal as signal
import itertools 
from PIL import Image

class Intensity:
    #All class functions can be run independently (do not need to run avg_intensity first)
    
    def __init__(self):
        self.cam = grabber.Webcam()
        
    def avg_intensity(self):
        #Just running fnc this will print the avg intensity,
        #but returns the value for use elsewhere
        self.rgb_list = self.cam.grab_image_data()
        #print rgb_list[1:100]

        rgb_avgs = []
        for element in self.rgb_list:
            #print element
            rgb_avgs.append(np.mean(list(element)))
            
        self.total_avg = np.mean(rgb_avgs)
        print "Average intensity is:"
        print self.total_avg
        return self.total_avg


    def intense_graph(self,num, delay = 0):
        #takes in number of desired picture samples, with some delay between 
        avg_read = []
        times = []
        timestart = timeit.time.time()
        #Creates dataset (Avg intensity, times of avg intensity)
        for i in range(0,num): #how many times to run
            avg_read.append(self.avg_intensity())
            times.append(timeit.time.time()-timestart)
            print "Working on iteration:" #makes sure it's not frozen
            print i+1
            time.sleep(delay)
        #print avg_read
        #print times
        #Butters filter setup
        N = 2 #order
        Wn = 0.05 #cutoff f
        B, A = signal.butter(N,Wn,output = 'ba')
        avg_readf = signal.filtfilt(B,A, avg_read)#filters the intensity data
        plt.plot(times,avg_read,'b')
        plt.plot(times,avg_readf,'r')
        plt.xlabel('Time in seconds')
        plt.ylabel('Average Intensity')
        plt.show()

    def daytime(self):
        #Run the function to print Daytime / nightime and return true / false
        self.avg_intensity()
        if self.total_avg > 70:
            print "It is daytime"
            return True
        else:
            print "It is nighttime"
            return False

    def common_color(self,n):
        rgb_list = self.cam.grab_image_data()
        occurance = {}
        #similar code to book assignment, creates list of common values
        for element in rgb_list:
            if element in occurance:
                occurance[element] +=1
            else:
                occurance[element] = 1
        occurance = sorted(occurance, key = occurance.get, reverse = True)
        print "Most common colors are:"
        print occurance[0:n]
        return occurance[0:n]

    def motion(self): #Motion detection function. Run it and it will return and print motion as boolean. 
        rgb_list1 = self.cam.grab_image_data()
        #print rgb_list1[1:100]
        rgb_list2 = self.cam.grab_image_data()
        #print "image list created"
        dist_list = []
        for i in range(0,len(rgb_list1)):
            rgb1 = list(rgb_list1[i])
            rgb2 = list(rgb_list2[i])
            dist_list.append(np.sqrt((rgb2[0]-rgb1[0])**2+(rgb2[1]-rgb1[1])**2+(rgb2[2]-rgb1[2])**2))
            
        #print dist_list[1:10]
        avg_dist = np.mean(dist_list)
        print "Average pixel distance is:"
        print avg_dist
        if avg_dist > 6: #Need to adjust this threshold when there's motion to test with!
            print "Motion Detected"
            return True
        else:
            print "No motion detected"
            return False

    def event(self): #This function, along with most of them, has issues when it's raining or at night
        #Center quad pixels: x: 225-575, y: 350-525 (center quad area)
        #Crop images to this:
        pic = self.cam.grab_image()
        #pic = Image.open('picture','r') This is event test image
        pic.show()
        half_width = pic.size[0]/2 #calculates half the image size, offsets from this calc
        half_height = pic.size[1]/2
        cropped = pic.crop((half_width-300,half_height-60,half_width+20,half_height+100)) #Crops the img
        cropped.show()
        rgb_list = list(cropped.getdata())
        rgb_list = self.cam.grab_image_data()
        #Average rgb value for empty square = 217,216,212 (calculated externally)
        no_event = [(217,216,212)]*len(rgb_list)#creates "image" of all pixels of most common rgb value, would like to replace with compaerison image of empty quad
        #Check image similarity (euclidian distance) w/ non-event range
        dist_list = []
        for i in range(0,len(rgb_list)):
            rgb1 = list(rgb_list[i])
            rgb2 = list(no_event[i])
            dist_list.append(np.sqrt((rgb2[0]-rgb1[0])**2+(rgb2[1]-rgb1[1])**2+(rgb2[2]-rgb1[2])**2))

        avg_dist = np.mean(dist_list)
        print "Average pixel distance from non-event average: "
        print avg_dist
        if avg_dist > 250: #Need to adjust this value in comparison to quad event
            print "There is an event in the quad"
            return True
        else:
            print "There is not an event in the quad"
            return False
        
if __name__ == "__main__":
    intense = Intensity()
    intense.daytime()
    intense.intense_graph(10)
    intense.common_color(3)
    intense.motion()
    intense.event()
        



        
