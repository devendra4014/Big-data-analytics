# observed data
x = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y = c(3, 5, 7, 9, 11, 13, 15, 17, 19, 21)

# check if x and y are related
covariance = cov(x, y)
print(covariance)

# check if the relationship is strong or weak
correlation = cor(x, y)
print(correlation)

# find the value of 7 for x = 15
# formula => y ~ x
# build the model
# simple linear regression
model = lm(formula = y ~ x)

# get all the information of the model
summary(model)

# predict the y value for x = 15
prediction = predict(model, data.frame(x=15))
print(class(prediction))

# predict the y value for x = 15, 16, 17, 18, 19, 20
# 1param: model
# 2param: 2 dimensional array
prediction = predict(model, data.frame(x=c(15, 16, 17, 18, 19, 20)))
print(prediction)


