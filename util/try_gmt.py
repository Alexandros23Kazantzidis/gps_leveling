import gmt

fig = gmt.Figure()

fig.coast(region=[-90, -70, 0, 20], projection='M6i', land='chocolate',
          frame=True)

fig.show()