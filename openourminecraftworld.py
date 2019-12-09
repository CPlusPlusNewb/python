#!/usr/bin/env python3

import webbrowser
a = input("Do you want to join our minecraft world? (y/n): ")


if (a == "y"):
  a_website = "https://classic.minecraft.net/?join=FDG4yuAcDpaBy8YQ"
  # Open url in a new window of the default browser, if possible
  webbrowser.open_new(a_website)
else:
  #if they say no (why did they open then, hell IDK)
  print ("Why the HECK did you open this then, smh")
