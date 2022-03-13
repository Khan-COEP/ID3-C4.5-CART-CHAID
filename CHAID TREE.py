def findDecision(obj): #obj[0]: temperature, obj[1]: humidity, obj[2]: visibility, obj[3]: wind_speed, obj[4]: cloud_cover, obj[5]: precip_intensity
	# {"feature": "cloud_cover", "instances": 3785, "metric_value": 389.5916, "depth": 1}
	if obj[4]<=0.40100660501981505:
		# {"feature": "humidity", "instances": 2043, "metric_value": 202.6655, "depth": 2}
		if obj[1]>0.6090553108174253:
			# {"feature": "temperature", "instances": 1063, "metric_value": 135.0024, "depth": 3}
			if obj[0]>57.86533396048918:
				# {"feature": "precip_intensity", "instances": 542, "metric_value": 97.2624, "depth": 4}
				if obj[5]<=0.003881918819188192:
					# {"feature": "wind_speed", "instances": 470, "metric_value": 60.1697, "depth": 5}
					if obj[3]<=4.137489361702127:
						# {"feature": "visibility", "instances": 287, "metric_value": 49.0358, "depth": 6}
						if obj[2]>9.617351916376307:
							return 'Clear'
						elif obj[2]<=9.617351916376307:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[3]>4.137489361702127:
						# {"feature": "visibility", "instances": 183, "metric_value": 21.1909, "depth": 6}
						if obj[2]>9.732513661202185:
							return 'Clear'
						elif obj[2]<=9.732513661202185:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Clear'
				elif obj[5]>0.003881918819188192:
					# {"feature": "wind_speed", "instances": 72, "metric_value": 20.1393, "depth": 5}
					if obj[3]<=3.833611111111111:
						# {"feature": "visibility", "instances": 39, "metric_value": 15.3333, "depth": 6}
						if obj[2]>8.95102564102564:
							return 'Drizzle'
						elif obj[2]<=8.95102564102564:
							return 'Drizzle'
						else: return 'Drizzle'
					elif obj[3]>3.833611111111111:
						# {"feature": "visibility", "instances": 33, "metric_value": 12.1618, "depth": 6}
						if obj[2]>8.64235730231548:
							return 'Drizzle'
						elif obj[2]<=8.64235730231548:
							return 'Drizzle'
						else: return 'Drizzle'
					else: return 'Drizzle'
				else: return 'Drizzle'
			elif obj[0]<=57.86533396048918:
				# {"feature": "wind_speed", "instances": 521, "metric_value": 52.468, "depth": 4}
				if obj[3]<=3.1261036468330134:
					# {"feature": "visibility", "instances": 344, "metric_value": 43.8593, "depth": 5}
					if obj[2]>9.659912790697675:
						# {"feature": "precip_intensity", "instances": 272, "metric_value": 20.5716, "depth": 6}
						if obj[5]<=0.0012:
							return 'Clear'
						elif obj[5]>0.0012:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[2]<=9.659912790697675:
						# {"feature": "precip_intensity", "instances": 72, "metric_value": 13.5465, "depth": 6}
						if obj[5]<=0.0:
							return 'Clear'
						elif obj[5]>0.0:
							return 'Drizzle'
						else: return 'Drizzle'
					else: return 'Clear'
				elif obj[3]>3.1261036468330134:
					# {"feature": "visibility", "instances": 177, "metric_value": 27.428, "depth": 5}
					if obj[2]>9.767344632768362:
						# {"feature": "precip_intensity", "instances": 127, "metric_value": 21.94, "depth": 6}
						if obj[5]<=0.0014:
							return 'Clear'
						elif obj[5]>0.0014:
							return 'Clear'
						else: return 'Clear'
					elif obj[2]<=9.767344632768362:
						# {"feature": "precip_intensity", "instances": 50, "metric_value": 2.0203, "depth": 6}
						if obj[5]<=0.0027:
							return 'Cloudy'
						elif obj[5]>0.0027:
							return 'Clear'
						else: return 'Clear'
					else: return 'Cloudy'
				else: return 'Clear'
			else: return 'Clear'
		elif obj[1]<=0.6090553108174253:
			# {"feature": "temperature", "instances": 980, "metric_value": 81.8172, "depth": 3}
			if obj[0]>65.47935714285715:
				# {"feature": "wind_speed", "instances": 500, "metric_value": 52.3406, "depth": 4}
				if obj[3]<=5.473:
					# {"feature": "visibility", "instances": 281, "metric_value": 38.8368, "depth": 5}
					if obj[2]>9.99:
						# {"feature": "precip_intensity", "instances": 247, "metric_value": 35.2855, "depth": 6}
						if obj[5]<=0.0018:
							return 'Clear'
						elif obj[5]>0.0018:
							return 'Drizzle'
						else: return 'Drizzle'
					elif obj[2]<=9.99:
						# {"feature": "precip_intensity", "instances": 34, "metric_value": 13.7473, "depth": 6}
						if obj[5]<=0.0016:
							return 'Clear'
						elif obj[5]>0.0016:
							return 'Drizzle'
						else: return 'Drizzle'
					else: return 'Clear'
				elif obj[3]>5.473:
					# {"feature": "visibility", "instances": 219, "metric_value": 15.1635, "depth": 5}
					if obj[2]>9.99:
						# {"feature": "precip_intensity", "instances": 196, "metric_value": 15.28, "depth": 6}
						if obj[5]<=0.0:
							return 'Clear'
						elif obj[5]>0.0:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[2]<=9.99:
						# {"feature": "precip_intensity", "instances": 23, "metric_value": 3.9788, "depth": 6}
						if obj[5]<=0.0008:
							return 'Cloudy'
						elif obj[5]>0.0008:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				else: return 'Clear'
			elif obj[0]<=65.47935714285715:
				# {"feature": "wind_speed", "instances": 480, "metric_value": 36.4652, "depth": 4}
				if obj[3]<=4.811041666666666:
					# {"feature": "visibility", "instances": 272, "metric_value": 24.3667, "depth": 5}
					if obj[2]>9.63:
						# {"feature": "precip_intensity", "instances": 267, "metric_value": 21.2044, "depth": 6}
						if obj[5]<=0.0:
							return 'Clear'
						else: return 'Clear'
					elif obj[2]<=9.63:
						return 'Cloudy'
					else: return 'Cloudy'
				elif obj[3]>4.811041666666666:
					# {"feature": "visibility", "instances": 208, "metric_value": 18.4728, "depth": 5}
					if obj[2]>9.98:
						# {"feature": "precip_intensity", "instances": 204, "metric_value": 18.5094, "depth": 6}
						if obj[5]<=0.0:
							return 'Clear'
						elif obj[5]>0.0:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[2]<=9.98:
						return 'Clear'
					else: return 'Clear'
				else: return 'Clear'
			else: return 'Clear'
		else: return 'Clear'
	elif obj[4]>0.40100660501981505:
		# {"feature": "precip_intensity", "instances": 1742, "metric_value": 220.9905, "depth": 2}
		if obj[5]>0.0:
			# {"feature": "humidity", "instances": 1021, "metric_value": 125.6324, "depth": 3}
			if obj[1]>0.8522820763956904:
				# {"feature": "temperature", "instances": 624, "metric_value": 86.2046, "depth": 4}
				if obj[0]>66.59391025641027:
					# {"feature": "wind_speed", "instances": 355, "metric_value": 68.6306, "depth": 5}
					if obj[3]>4.9092112676056345:
						# {"feature": "visibility", "instances": 182, "metric_value": 37.8957, "depth": 6}
						if obj[2]>7.558021978021977:
							return 'Cloudy'
						elif obj[2]<=7.558021978021977:
							return 'Drizzle'
						else: return 'Drizzle'
					elif obj[3]<=4.9092112676056345:
						# {"feature": "visibility", "instances": 173, "metric_value": 45.2027, "depth": 6}
						if obj[2]>7.551560693641619:
							return 'Cloudy'
						elif obj[2]<=7.551560693641619:
							return 'Drizzle'
						else: return 'Drizzle'
					else: return 'Drizzle'
				elif obj[0]<=66.59391025641027:
					# {"feature": "visibility", "instances": 269, "metric_value": 37.5146, "depth": 5}
					if obj[2]<=9.239763986979627:
						# {"feature": "wind_speed", "instances": 214, "metric_value": 31.3669, "depth": 6}
						if obj[3]<=4.201214953271028:
							return 'Cloudy'
						elif obj[3]>4.201214953271028:
							return 'Drizzle'
						else: return 'Drizzle'
					elif obj[2]>9.239763986979627:
						# {"feature": "wind_speed", "instances": 55, "metric_value": 22.5599, "depth": 6}
						if obj[3]<=5.609818181818182:
							return 'Cloudy'
						elif obj[3]>5.609818181818182:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				else: return 'Cloudy'
			elif obj[1]<=0.8522820763956904:
				# {"feature": "wind_speed", "instances": 397, "metric_value": 62.9819, "depth": 4}
				if obj[3]<=5.931788413098237:
					# {"feature": "temperature", "instances": 207, "metric_value": 30.2243, "depth": 5}
					if obj[0]>69.22700483091788:
						# {"feature": "visibility", "instances": 134, "metric_value": 26.6992, "depth": 6}
						if obj[2]>9.459179104477613:
							return 'Drizzle'
						elif obj[2]<=9.459179104477613:
							return 'Drizzle'
						else: return 'Drizzle'
					elif obj[0]<=69.22700483091788:
						# {"feature": "visibility", "instances": 73, "metric_value": 14.9551, "depth": 6}
						if obj[2]>8.02035234596307:
							return 'Cloudy'
						elif obj[2]<=8.02035234596307:
							return 'Overcast'
						else: return 'Overcast'
					else: return 'Cloudy'
				elif obj[3]>5.931788413098237:
					# {"feature": "temperature", "instances": 190, "metric_value": 46.0105, "depth": 5}
					if obj[0]>70.934:
						# {"feature": "visibility", "instances": 110, "metric_value": 26.2043, "depth": 6}
						if obj[2]>9.342909090909092:
							return 'Drizzle'
						elif obj[2]<=9.342909090909092:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[0]<=70.934:
						# {"feature": "visibility", "instances": 80, "metric_value": 20.3664, "depth": 6}
						if obj[2]>9.582125:
							return 'Cloudy'
						elif obj[2]<=9.582125:
							return 'Drizzle'
						else: return 'Drizzle'
					else: return 'Cloudy'
				else: return 'Cloudy'
			else: return 'Drizzle'
		elif obj[5]<=0.0:
			# {"feature": "wind_speed", "instances": 721, "metric_value": 101.4645, "depth": 3}
			if obj[3]<=5.608404993065188:
				# {"feature": "humidity", "instances": 380, "metric_value": 55.6805, "depth": 4}
				if obj[1]>0.8171052631578948:
					# {"feature": "temperature", "instances": 224, "metric_value": 40.7866, "depth": 5}
					if obj[0]>61.10870535714286:
						# {"feature": "visibility", "instances": 123, "metric_value": 15.6604, "depth": 6}
						if obj[2]>8.313252032520325:
							return 'Cloudy'
						elif obj[2]<=8.313252032520325:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[0]<=61.10870535714286:
						# {"feature": "visibility", "instances": 101, "metric_value": 29.0173, "depth": 6}
						if obj[2]>8.207722772277227:
							return 'Cloudy'
						elif obj[2]<=8.207722772277227:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				elif obj[1]<=0.8171052631578948:
					# {"feature": "temperature", "instances": 156, "metric_value": 22.7232, "depth": 5}
					if obj[0]>59.30858974358974:
						return 'Cloudy'
					elif obj[0]<=59.30858974358974:
						# {"feature": "visibility", "instances": 77, "metric_value": 14.5042, "depth": 6}
						if obj[2]>9.634805194805194:
							return 'Cloudy'
						elif obj[2]<=9.634805194805194:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				else: return 'Cloudy'
			elif obj[3]>5.608404993065188:
				# {"feature": "humidity", "instances": 341, "metric_value": 53.0504, "depth": 4}
				if obj[1]>0.7576246334310851:
					# {"feature": "temperature", "instances": 186, "metric_value": 39.9053, "depth": 5}
					if obj[0]>67.60645161290323:
						# {"feature": "visibility", "instances": 96, "metric_value": 26.326, "depth": 6}
						if obj[2]>8.590625000000001:
							return 'Cloudy'
						elif obj[2]<=8.590625000000001:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[0]<=67.60645161290323:
						# {"feature": "visibility", "instances": 90, "metric_value": 17.3989, "depth": 6}
						if obj[2]>9.241555555555555:
							return 'Cloudy'
						elif obj[2]<=9.241555555555555:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				elif obj[1]<=0.7576246334310851:
					# {"feature": "visibility", "instances": 155, "metric_value": 20.2027, "depth": 5}
					if obj[2]>9.82883870967742:
						# {"feature": "temperature", "instances": 121, "metric_value": 16.6189, "depth": 6}
						if obj[0]>63.179008264462816:
							return 'Cloudy'
						elif obj[0]<=63.179008264462816:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[2]<=9.82883870967742:
						return 'Cloudy'
					else: return 'Cloudy'
				else: return 'Cloudy'
			else: return 'Cloudy'
		else: return 'Cloudy'
	else: return 'Cloudy'
