model4 = keras.Sequential()
# model4.add(keras.layers.Embedding(500, 16, input_length=100))
# model4.add(keras.layers.GRU(8))
# model4.add(keras.layers.Dense(1, activation='sigmoid'))
# model4.summary()

# rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
# model4.compile(optimizer=rmsprop,loss='binary_crossentropy', metrics=['accuracy']) # 모델 컴파일
# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-gru-model.h5')
# early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
# history = model4.fit(train_seq, train_target, epochs=100, batch_size=64, validation_data=(val_seq, val_target), 
#                     callbacks=[checkpoint_cb, early_stopping_cb])

# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend(['train', 'val'])