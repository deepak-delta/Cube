# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:50:18 2019

@author: DEEPAK D KRISHNA
"""


class Combine:

    def sides(self, sides):
        """Join all the sides together into one single string.

        :param sides: dictionary with all the sides
        :returns: string
        """
        combined = ''
        for face in 'URFDLB':
            combined += ''.join(sides[face])
        return combined

combine = Combine()
