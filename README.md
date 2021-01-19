# rivers_and_streams
Create a measure of rivers and streams by geographical boundaries in the continental United States


only named rivers and streams in order to only county each river/stream once per county


in base case .length returns lengths in meters that are roughly equivalent
to mileage given in raw data (i.e. total length in 'miles' of named rivers
in IN is 8547.95, whereas total length in meters using .length is 13726886.76
which is equivalent to 8529.49 miles
the ratio of .length to raw data total is: 8529.49/8547.95 = 0.9978
ratio for IN once split and calculated by county is 13866.08km == 8615.98 miles
which represnets and over reporting of 1.00795, less than 1%
