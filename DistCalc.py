def DistanceFromFocus(PixelInfo,maxdist,FocalPoint,distx=1,distz=1):
    focusdist = ((distx*((PixelInfo[0] - FocalPoint[0])**2 + (PixelInfo[1] - FocalPoint[1])**2) + distz*(PixelInfo[2] - FocalPoint[2])**2)**0.5)/maxdist
    return PixelInfo[3] - round(focusdist*PixelInfo[3])


def MaxDistance(width,length,distx=1, distz=1):
    return (((distx*width)**2+(distx*length)**2+(distz*255)**2)**0.5)