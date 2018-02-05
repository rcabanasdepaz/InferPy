import inferpy as inf

# define a 2-dimension Normal distribution of 2·3=6 batches
with inf.replicate(size=2):
	with inf.replicate(size=3):
		x = inf.models.Normal(loc=0., scale=1., dim=2)


# print its parameters
print(x.loc)
print(x.scale)
print(x.shape)

# get a sample
sample_x = x.sample([4,10])

# the shape of the sample is (4, 10, 6, 2)
print(sample_x.shape)