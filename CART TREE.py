def findDecision(obj): #obj[0]: temperature, obj[1]: humidity, obj[2]: visibility, obj[3]: wind_speed, obj[4]: cloud_cover, obj[5]: precip_intensity
	# {"feature": "cloud_cover", "instances": 3785, "metric_value": 0.4528, "depth": 1}
	if obj[4]<=0.40100660501981505:
		# {"feature": "precip_intensity", "instances": 2043, "metric_value": 0.3191, "depth": 2}
		if obj[5]<=0.0:
			# {"feature": "visibility", "instances": 1853, "metric_value": 0.266, "depth": 3}
			if obj[2]>9.858267674042095:
				# {"feature": "wind_speed", "instances": 1482, "metric_value": 0.2082, "depth": 4}
				if obj[3]<=12.661978703525499:
					# {"feature": "temperature", "instances": 1465, "metric_value": 0.2043, "depth": 5}
					if obj[0]<=74.77325015564583:
						# {"feature": "humidity", "instances": 1192, "metric_value": 0.1757, "depth": 6}
						if obj[1]>0.39707868029044374:
							return 'Clear'
						elif obj[1]<=0.39707868029044374:
							return 'Clear'
						else: return 'Clear'
					elif obj[0]>74.77325015564583:
						# {"feature": "humidity", "instances": 273, "metric_value": 0.3092, "depth": 6}
						if obj[1]>0.30884729004475686:
							return 'Clear'
						elif obj[1]<=0.30884729004475686:
							return 'Clear'
						else: return 'Clear'
					else: return 'Clear'
				elif obj[3]>12.661978703525499:
					# {"feature": "humidity", "instances": 17, "metric_value": 0.2059, "depth": 5}
					if obj[1]<=0.66:
						# {"feature": "temperature", "instances": 16, "metric_value": 0.2045, "depth": 6}
						if obj[0]>56.8:
							return 'Cloudy'
						elif obj[0]<=56.8:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[1]>0.66:
						return 'Clear'
					else: return 'Clear'
				else: return 'Cloudy'
			elif obj[2]<=9.858267674042095:
				# {"feature": "wind_speed", "instances": 371, "metric_value": 0.408, "depth": 4}
				if obj[3]<=3.7177358490566035:
					# {"feature": "humidity", "instances": 223, "metric_value": 0.3323, "depth": 5}
					if obj[1]>0.6417254078897482:
						# {"feature": "temperature", "instances": 216, "metric_value": 0.323, "depth": 6}
						if obj[0]<=64.6239928263033:
							return 'Clear'
						elif obj[0]>64.6239928263033:
							return 'Clear'
						else: return 'Clear'
					elif obj[1]<=0.6417254078897482:
						# {"feature": "temperature", "instances": 7, "metric_value": 0.2381, "depth": 6}
						if obj[0]<=62.22:
							return 'Cloudy'
						elif obj[0]>62.22:
							return 'Clear'
						else: return 'Clear'
					else: return 'Cloudy'
				elif obj[3]>3.7177358490566035:
					# {"feature": "humidity", "instances": 148, "metric_value": 0.4702, "depth": 5}
					if obj[1]>0.761554054054054:
						# {"feature": "temperature", "instances": 84, "metric_value": 0.4611, "depth": 6}
						if obj[0]>48.35476452417807:
							return 'Cloudy'
						elif obj[0]<=48.35476452417807:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[1]<=0.761554054054054:
						# {"feature": "temperature", "instances": 64, "metric_value": 0.4395, "depth": 6}
						if obj[0]>37.602426784482844:
							return 'Clear'
						elif obj[0]<=37.602426784482844:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Clear'
				else: return 'Cloudy'
			else: return 'Clear'
		elif obj[5]>0.0:
			# {"feature": "temperature", "instances": 190, "metric_value": 0.6696, "depth": 3}
			if obj[0]>52.333098946137156:
				# {"feature": "humidity", "instances": 183, "metric_value": 0.6685, "depth": 4}
				if obj[1]>0.480804499067693:
					# {"feature": "wind_speed", "instances": 179, "metric_value": 0.6663, "depth": 5}
					if obj[3]<=8.423820289403015:
						# {"feature": "visibility", "instances": 172, "metric_value": 0.6633, "depth": 6}
						if obj[2]>9.305755813953487:
							return 'Drizzle'
						elif obj[2]<=9.305755813953487:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[3]>8.423820289403015:
						# {"feature": "visibility", "instances": 7, "metric_value": 0.3571, "depth": 6}
						if obj[2]<=9.96:
							return 'Clear'
						elif obj[2]>9.96:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				elif obj[1]<=0.480804499067693:
					# {"feature": "wind_speed", "instances": 4, "metric_value": 0.0, "depth": 5}
					if obj[3]<=3.77:
						return 'Clear'
					elif obj[3]>3.77:
						return 'Cloudy'
					else: return 'Cloudy'
				else: return 'Clear'
			elif obj[0]<=52.333098946137156:
				# {"feature": "humidity", "instances": 7, "metric_value": 0.2381, "depth": 4}
				if obj[1]>0.54:
					# {"feature": "wind_speed", "instances": 6, "metric_value": 0.0, "depth": 5}
					if obj[3]>2.91:
						return 'Clear'
					elif obj[3]<=2.91:
						return 'Cloudy'
					else: return 'Cloudy'
				elif obj[1]<=0.54:
					return 'Cloudy'
				else: return 'Cloudy'
			else: return 'Clear'
		else: return 'Cloudy'
	elif obj[4]>0.40100660501981505:
		# {"feature": "precip_intensity", "instances": 1742, "metric_value": 0.3649, "depth": 2}
		if obj[5]<=0.010697933409873708:
			# {"feature": "visibility", "instances": 1374, "metric_value": 0.3564, "depth": 3}
			if obj[2]>5.591470180346073:
				# {"feature": "temperature", "instances": 1279, "metric_value": 0.3367, "depth": 4}
				if obj[0]>65.24996090695856:
					# {"feature": "humidity", "instances": 719, "metric_value": 0.3425, "depth": 5}
					if obj[1]>0.818317107093185:
						# {"feature": "wind_speed", "instances": 431, "metric_value": 0.4115, "depth": 6}
						if obj[3]>5.021160092807424:
							return 'Cloudy'
						elif obj[3]<=5.021160092807424:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[1]<=0.818317107093185:
						# {"feature": "wind_speed", "instances": 288, "metric_value": 0.2314, "depth": 6}
						if obj[3]>3.881762874176848:
							return 'Cloudy'
						elif obj[3]<=3.881762874176848:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				elif obj[0]<=65.24996090695856:
					# {"feature": "humidity", "instances": 560, "metric_value": 0.3174, "depth": 5}
					if obj[1]<=0.9171396368745562:
						# {"feature": "wind_speed", "instances": 468, "metric_value": 0.2886, "depth": 6}
						if obj[3]<=8.599615532282481:
							return 'Cloudy'
						elif obj[3]>8.599615532282481:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[1]>0.9171396368745562:
						# {"feature": "wind_speed", "instances": 92, "metric_value": 0.4324, "depth": 6}
						if obj[3]<=8.66488813387285:
							return 'Cloudy'
						elif obj[3]>8.66488813387285:
							return 'Overcast'
						else: return 'Overcast'
					else: return 'Cloudy'
				else: return 'Cloudy'
			elif obj[2]<=5.591470180346073:
				# {"feature": "wind_speed", "instances": 95, "metric_value": 0.5287, "depth": 4}
				if obj[3]<=4.141157894736841:
					# {"feature": "humidity", "instances": 57, "metric_value": 0.4029, "depth": 5}
					if obj[1]>0.9:
						# {"feature": "temperature", "instances": 56, "metric_value": 0.4003, "depth": 6}
						if obj[0]>60.285178571428574:
							return 'Cloudy'
						elif obj[0]<=60.285178571428574:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[1]<=0.9:
						return 'Overcast'
					else: return 'Overcast'
				elif obj[3]>4.141157894736841:
					# {"feature": "temperature", "instances": 38, "metric_value": 0.6241, "depth": 5}
					if obj[0]>61.28244303455446:
						# {"feature": "humidity", "instances": 35, "metric_value": 0.6229, "depth": 6}
						if obj[1]>0.89:
							return 'Overcast'
						elif obj[1]<=0.89:
							return 'Humid and Cloudy'
						else: return 'Humid and Cloudy'
					elif obj[0]<=61.28244303455446:
						return 'Cloudy'
					else: return 'Cloudy'
				else: return 'Overcast'
			else: return 'Cloudy'
		elif obj[5]>0.010697933409873708:
			# {"feature": "humidity", "instances": 368, "metric_value": 0.3553, "depth": 3}
			if obj[1]>0.8592934782608697:
				# {"feature": "temperature", "instances": 224, "metric_value": 0.4499, "depth": 4}
				if obj[0]>44.67552719631827:
					# {"feature": "wind_speed", "instances": 217, "metric_value": 0.459, "depth": 5}
					if obj[3]<=10.585353404277102:
						# {"feature": "visibility", "instances": 212, "metric_value": 0.4658, "depth": 6}
						if obj[2]>3.27:
							return 'Drizzle'
						elif obj[2]<=3.27:
							return 'Rain'
						else: return 'Rain'
					elif obj[3]>10.585353404277102:
						return 'Drizzle'
					else: return 'Drizzle'
				elif obj[0]<=44.67552719631827:
					return 'Drizzle'
				else: return 'Drizzle'
			elif obj[1]<=0.8592934782608697:
				# {"feature": "visibility", "instances": 144, "metric_value": 0.1865, "depth": 4}
				if obj[2]>6.11:
					# {"feature": "wind_speed", "instances": 143, "metric_value": 0.1867, "depth": 5}
					if obj[3]>2.96042226417134:
						# {"feature": "temperature", "instances": 122, "metric_value": 0.2023, "depth": 6}
						if obj[0]>58.87351653211391:
							return 'Drizzle'
						elif obj[0]<=58.87351653211391:
							return 'Drizzle'
						else: return 'Drizzle'
					elif obj[3]<=2.96042226417134:
						# {"feature": "temperature", "instances": 21, "metric_value": 0.0794, "depth": 6}
						if obj[0]>69.61:
							return 'Drizzle'
						elif obj[0]<=69.61:
							return 'Drizzle'
						else: return 'Drizzle'
					else: return 'Drizzle'
				elif obj[2]<=6.11:
					return 'Rain'
				else: return 'Rain'
			else: return 'Drizzle'
		else: return 'Drizzle'
	else: return 'Cloudy'
