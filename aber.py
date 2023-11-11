from pylab import *
from pandas import *
def otto(p_min,p_max,v_max,r,gamma):
    font = {'family' : 'Times New Roman','size' : 39}
    figure(figsize=(15,10))
    rc('font', **font)
    '''This function prints Otto cycle
    arguments are as follows:
    _min: minimum pressure
    p_max: Maximum pressure
    v_max: Maximum volume
    r: compression ratio
    gma: Adiabatic exponent
    The order of arguments is:
    p_min,p_max,v_max,r,gma
    '''

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # Process 1-2
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    p1 = p_min
    v1 = v_max
    v2 = v1 / r
    c1 = p1 * v1 ** gamma
    v = linspace(v2, v1, 100) # 100 points between v2 and v1
    p = c1 / v ** gamma
    plot(v, p / 1000, 'b', linewidth=3)


    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # Process 2-3
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    p3 = p_max
    v3 = v2
    p2 = c1 / v2 ** gamma
    p = linspace(p2, p3, 100)# 100 points between p2 and p3
    v = 100 * [v3]
    plot(v, p / 1000, 'r', linewidth=3)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # Process 3-4
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    c2 = p3 * v3 ** gamma 
    v4 = v1
    v = linspace(v3, v4, 100)
    p = c2 / v ** gamma
    plot(v, p / 1000, 'g', linewidth=3)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # Process 4-1
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    v4 = v1
    p4 = c2 / v4 ** gamma
    p = linspace(p1, p4, 100)
    v = 100 * [v1]
    plot(v, p / 1000, 'o', linewidth=3)
    title('Otto Cycle', size='xx-large', color='k')
    xlabel('Volume ($m^3$)')
    ylabel('Pressure (kPa)')
    text(v1,p1/1000-30,'1')
    text(v2,p2/1000-200,'2')
    text(v3+0.01,p3/1000-20,'3')
    text(v4,p4/1000+10,'4')
    data={'p':[p1,p2,p3,p4],
        'v':[v1,v2,v3,v4],
        'c':[c1,'' ,c2,'' ],
        'State': [1,2,3,4]}
    df=DataFrame(data)
    savefig('Otto_final.jpg')
    return df.set_index('State')
oc=otto(2*10**5,35*10**5,0.5,5,1.4)
show()
oc