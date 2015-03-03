#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
dicemanHoliday.py v0.1
Plan your travels the Diceman way

##############################################################################
# Released as open source by Tom Watson                                      #
#                                                                            #
# Developed by Tom Watson, http://www.github.com/tfwiii                      #
#                                                                            #
# Released under the GNU Affero General Public License                       #
# (http://www.gnu.org/licenses/agpl-3.0.html)                                #
##############################################################################

Usage examples:
Just run it!

Read the README for more details
"""

import sys
from random import *   
from math import *
from time import *


countries = [
        [
            'North America', 
            'Antigua and Barbuda', 
            'Bahamas', 
            'Barbados', 
            'Belize', 
            'Canada', 
            'Costa Rica', 
            'Cuba', 
            'Dominica', 
            'Dominican Republic', 
            'El Salvador', 
            'Grenada', 
            'Guatemala', 
            'Haiti', 
            'Honduras', 
            'Jamaica', 
            'Mexico', 
            'Nicaragua', 
            'Panama', 
            'Saint Kitts and Nevis', 
            'Saint Lucia', 
            'Saint Vincent and the Grenadines', 
            'Trinidad and Tobago', 
            'United States'
        ], 
        [
            'Africa', 
            'Algeria', 
            'Angola', 
            'Benin', 
            'Botswana', 
            'Burkina', 
            'Burundi', 
            'Cameroon', 
            'Cape Verde', 
            'Central African Republic', 
            'Chad', 
            'Comoros', 
            'Congo', 
            'Democratic Republic of Congo', 
            'Djibouti', 
            'Egypt', 
            'Equatorial Guinea', 
            'Eritrea', 
            'Ethiopia', 
            'Gabon', 
            'Gambia', 
            'Ghana', 
            'Guinea', 
            'Guinea-Bissau', 
            'Ivory Coast', 
            'Kenya', 
            'Lesotho', 
            'Liberia', 
            'Libya', 
            'Madagascar', 
            'Malawi', 
            'Mali', 
            'Mauritania', 
            'Mauritius', 
            'Morocco', 
            'Mozambique',
            'Namibia', 
            'Niger', 
            'Nigeria', 
            'Rwanda', 
            'Sao Tome and Principe', 
            'Senegal', 
            'Seychelles', 
            'Sierra Leone', 
            'Somalia', 
            'South Africa', 
            'South Sudan', 
            'Sudan', 
            'Swaziland', 
            'Tanzania', 
            'Togo', 
            'Tunisia', 
            'Uganda', 
            'Zambia', 
            'Zimbabwe'
        ], 
        [
            'Europe', 
            'Albania', 
            'Andorra', 
            'Armenia', 
            'Austria', 
            'Azerbaijan', 
            'Belarus', 
            'Belgium', 
            'Bosnia and Herzegovina', 
            'Bulgaria', 
            'Croatia', 
            'Cyprus', 
            'Czech Republic', 
            'Denmark', 
            'Estonia', 
            'Finland', 
            'France', 
            'Georgia', 
            'Germany', 
            'Greece', 
            'Hungary', 
            'Iceland', 
            'Ireland', 
            'Italy', 
            'Latvia', 
            'Liechtenstein', 
            'Lithuania', 
            'Luxembourg', 
            'Macedonia', 
            'Malta', 
            'Moldova', 
            'Monaco', 
            'Montenegro', 
            'Netherlands', 
            'Norway', 
            'Poland', 
            'Portugal', 
            'Romania', 
            'San Marino', 
            'Serbia', 
            'Slovakia', 
            'Slovenia', 
            'Spain', 
            'Sweden', 
            'Switzerland', 
            'Ukraine', 
            'United Kingdom', 
            'Vatican City'
        ], 
        [
            'Oceana', 
            'Australia', 
            'Fiji', 
            'Kiribati', 
            'Marshall Islands', 
            'Micronesia', 
            'Nauru', 
            'New Zealand', 
            'Palau', 
            'Papua New Guinea', 
            'Samoa', 
            'Solomon Islands', 
            'Tonga', 
            'Tuvalu', 
            'Vanuatu'
        ], 
        [
            'South America', 
            'Argentina', 
            'Bolivia', 
            'Brazil', 
            'Chile', 
            'Colombia', 
            'Ecuador', 
            'Guyana', 
            'Paraguay', 
            'Peru', 
            'Suriname', 
            'Uruguay', 
            'Venezuela'
        ], 
        [
            'Asia', 
            'Afghanistan', 
            'Bahrain', 
            'Bangladesh', 
            'Bhutan', 
            'Brunei', 
            'Burma (Myanmar)', 
            'Cambodia', 
            'China', 
            'East Timor', 
            'India', 
            'Indonesia', 
            'Iran', 
            'Iraq', 
            'Israel', 
            'Japan', 
            'Jordan', 
            'Kazakhstan', 
            'North Korea', 
            'South Korea', 
            'Kuwait', 
            'Kyrgyzstan', 
            'Laos', 
            'Lebanon', 
            'Malaysia', 
            'Maldives', 
            'Mongolia', 
            'Nepal', 
            'Oman', 
            'Pakistan', 
            'Philippines', 
            'Qatar', 
            'Russian Federation', 
            'Saudi Arabia', 
            'Singapore', 
            'Sri Lanka', 
            'Syria', 
            'Tajikistan', 
            'Thailand', 
            'Turkey', 
            'Turkmenistan', 
            'United Arab Emirates', 
            'Uzbekistan', 
            'Vietnam', 
            'Yemen'
        ]
    ]


def rollDie(duration):
    currentRoll = 0
    for x in range(duration):
	currentRoll = randint(1,6)
	print '%d' % currentRoll,
	sys.stdout.flush()
	sleep(0.1)
	print '\r',
	sys.stdout.flush()
    print ''
    return currentRoll
	

def get_continent():
    sleep(1)
    roll = rollDie(10) 
    print "Rolled %d - %s" % (roll, countries[roll-1][0]) 
    return roll-1 


def get_country(candidate):
    print 'Choosing country %d' % (candidate+1)
    country = ''
    continent = get_continent() 
    country_candidates = countries[continent][1:]
    num_of_countries = len(country_candidates)
    while num_of_countries > 5:
        chunk = ceil(num_of_countries/6.0)
        sleep(1)
        roll = rollDie(10) 
        while roll*chunk > num_of_countries:
            print 'Rolled %d - No match - rolling again.' % roll
            roll = rollDie(10) 
        start_slice = int((chunk*roll)-chunk)
        end_slice = int(chunk*roll)
        country_candidates = country_candidates[start_slice:end_slice]
        num_of_countries = len(country_candidates)
        print "Rolled %d - %s" % (roll, ', '.join(country_candidates))
    sleep(1)
    roll = rollDie(5)
    while roll > num_of_countries:
        print 'Rolled %d - No match - rolling again.' % roll
	roll = rollDie(10)
    country = country_candidates[roll-1]
    print 'Rolled %d' % roll
    print 'Country %d is %s' % (candidate + 1, country)
    print ''
    return country


def get_country_choices():
    choices = [get_country(x) for x in range(6)]
    return choices


def final_decision(choices):
    print "Rolling for the final decision..."
    roll = rollDie(20) 
    return choices[roll-1]


def main():
    print """
               .........
               :~, *   * ~,
               : ~, *   * ~.
               :  ~........~
               : *:         :      ~'~,
               :  :         :    ~' *  ~,
               ~* :    *    : ,~' *    * ~,
                ~,:         :.~,*    *  ,~ :
                 ~:.........::  ~, *  ,~   :
                             : *  ~,,~  *  :
                             :* * * :  *   :
 Diceman Holiday              ~, *  : *  ,~
                                ~,  :  ,~
 Inspired by Luke Rhinehart       ~,:,~
                                  
 http://en.wikipedia.org/wiki/The_Dice_Man

 Tom Watson, http://www.github.com/tfwiii 
     
 Released under the GNU Affero General Public License
 (http://www.gnu.org/licenses/agpl-3.0.html)
    
    """ 
    choices = get_country_choices()
    print 'You are going to one of: ' + ', '.join(choices) + '...'
    destination = final_decision(choices)
    print "Congratulations, you're going to %s!" % destination

__version__ = '0.1'
if __name__ == '__main__':
    main()
