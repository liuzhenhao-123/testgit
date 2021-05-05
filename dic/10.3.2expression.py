import pandas as pd
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
sfm=SelectFromModel(RandomForestRegressor(n_estimators=100,
                                          random_state=38),
                    threshold='median')
sfm.fit(X_train_scaled,y_train)
X_train_sfm=sfm.transform(X_train_scaled)
print(X_train_sfm.shape)

