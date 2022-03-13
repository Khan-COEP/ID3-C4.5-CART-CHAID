def findDecision(obj): #obj[0]: temperature, obj[1]: humidity, obj[2]: visibility, obj[3]: wind_speed, obj[4]: cloud_cover, obj[5]: precip_intensity
	# {"feature": "visibility", "instances": 3785, "metric_value": 1.8, "depth": 1}
	if obj[2]>1.81:
		# {"feature": "precip_intensity", "instances": 3784, "metric_value": 1.797, "depth": 2}
		if obj[5]<=0.005533298097251586:
			# {"feature": "cloud_cover", "instances": 3233, "metric_value": 1.3202, "depth": 3}
			if obj[4]<=0.35418187442004334:
				# {"feature": "humidity", "instances": 1867, "metric_value": 0.6359, "depth": 4}
				if obj[1]<=0.9731145556794227:
					# {"feature": "wind_speed", "instances": 1866, "metric_value": 0.6348, "depth": 5}
					if obj[3]<=12.14378536866854:
						# {"feature": "temperature", "instances": 1847, "metric_value": 0.6228, "depth": 6}
						if obj[0]<=88.1235815859914:
							return 'Clear'
						elif obj[0]>88.1235815859914:
							return 'Clear'
						else: return 'Clear'
					elif obj[3]>12.14378536866854:
						# {"feature": "temperature", "instances": 19, "metric_value": 0.9495, "depth": 6}
						if obj[0]>53.47:
							return 'Cloudy'
						elif obj[0]<=53.47:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				elif obj[1]>0.9731145556794227:
					return 'Cloudy'
				else: return 'Cloudy'
			elif obj[4]>0.35418187442004334:
				# {"feature": "temperature", "instances": 1366, "metric_value": 0.7032, "depth": 4}
				if obj[0]<=75.25989668621719:
					# {"feature": "wind_speed", "instances": 1181, "metric_value": 0.7231, "depth": 5}
					if obj[3]<=13.652779134074748:
						# {"feature": "humidity", "instances": 1169, "metric_value": 0.7281, "depth": 6}
						if obj[1]>0.5756017983415751:
							return 'Cloudy'
						elif obj[1]<=0.5756017983415751:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[3]>13.652779134074748:
						return 'Cloudy'
					else: return 'Cloudy'
				elif obj[0]>75.25989668621719:
					# {"feature": "humidity", "instances": 185, "metric_value": 0.4438, "depth": 5}
					if obj[1]<=0.8662788711109782:
						# {"feature": "wind_speed", "instances": 152, "metric_value": 0.3477, "depth": 6}
						if obj[3]>1.8914508055418775:
							return 'Cloudy'
						elif obj[3]<=1.8914508055418775:
							return 'Cloudy'
						else: return 'Cloudy'
					elif obj[1]>0.8662788711109782:
						# {"feature": "wind_speed", "instances": 33, "metric_value": 0.6312, "depth": 6}
						if obj[3]>4.989061653085941:
							return 'Cloudy'
						elif obj[3]<=4.989061653085941:
							return 'Cloudy'
						else: return 'Cloudy'
					else: return 'Cloudy'
				else: return 'Cloudy'
			else: return 'Cloudy'
		elif obj[5]>0.005533298097251586:
			# {"feature": "humidity", "instances": 551, "metric_value": 0.7313, "depth": 3}
			if obj[1]>0.6211745001192835:
				# {"feature": "cloud_cover", "instances": 524, "metric_value": 0.7535, "depth": 4}
				if obj[4]>0.24283825760660965:
					# {"feature": "temperature", "instances": 510, "metric_value": 0.7656, "depth": 5}
					if obj[0]>52.25465736883514:
						# {"feature": "wind_speed", "instances": 497, "metric_value": 0.7772, "depth": 6}
						if obj[3]<=13.155093051095095:
							return 'Drizzle'
						elif obj[3]>13.155093051095095:
							return 'Drizzle'
						else: return 'Drizzle'
					elif obj[0]<=52.25465736883514:
						return 'Drizzle'
					else: return 'Drizzle'
				elif obj[4]<=0.24283825760660965:
					return 'Drizzle'
				else: return 'Drizzle'
			elif obj[1]<=0.6211745001192835:
				return 'Drizzle'
			else: return 'Drizzle'
		else: return 'Drizzle'
	elif obj[2]<=1.81:
		return 'Foggy'
	else: return 'Foggy'
