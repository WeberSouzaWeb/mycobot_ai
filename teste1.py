def show_video_v2(self):
    #self.robot.init_robot()
    xyz = np.array ([0,0,0])
    LIST = []
    num_count = 0
    list_len = 5
    #cmax = [180, 80, 240]
    #cmin = [130, 80, 200]
    cmax = [150, 150, 300]
    cmin = [-150, 250, 200]

    while cv2.waitKey(1) < 0:
        success, img = self.cap.read()
        if not success:
            print("It seems that the image cannot be acquired correctly.")
            break
        # transfrom the ing to model of gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Detect ArUco marker.
        corners, ids, rejectImaPoint = cv2.aruco.detectMarkers (gray, self.aruco_dict, parameters=self.aruco_params)
        
        if len(corners) > 0:
            if ids is not None:
                #get informations of aruco
                ret = cv2.aruco.estimatePoseSingleMarkers( corners, 0.025, self.camera matrix, self.dist_coeffs)
                #'''https://stackoverflow.com/questions/53303730/what-is-the-value-for-markerlength-in-aruco-estimateposesinglemarkers'''
                
                #rvec:rotation offset, tvec: translation deviator (rvec, tvec) = (ret[0], ret[1])
                (rvec tvec).any() xyz = tvec[0, 0, :) * 1000 гру = rvec [0,0,:]
                camera = np.array([xyz [0], xyz [1], xyz[2]])
                if num_count > list_len: 
                    target = model_track(camera)
                    print("target", target)
                    for i in range(3):
                        if target [i] > cmax[i]:
                            target [i] = cmax[i]
                        if target [i] < cmin[i]:
                            target[i] = cmin[i]

                    pose = np.array([-103, 8.9, -164])
                    coord = np.concatenate ((target.copy(), pose), axis=0)

                    #q1 = math.atan(xyz [0] / xyz [2])*180/np.pi 
                    mc.send_coords (coord, 50,0)

                    #print('target', coord)
                    num count = 1
                else:
                num count = num count + 1
                for i in range(rvec.shape[0]):
                #draw the aruco on img
                cv2.aruco.drawDetectedMarkers (img, corners)
                cv2.imshow("show video", img)