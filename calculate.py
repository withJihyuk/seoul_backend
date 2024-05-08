import math

def distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # 위도와 경도의 차이를 구함
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # 구 방정식을 사용하여 거리 계산
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # 지구 반지름을 곱해 실제 거리 계산

    return distance

def find_nearest_events(target_lat, target_lon, events_data, num_closest):
    closest_events = []
    for event in events_data:
        event_lat = event["LAT"]
        event_lon = event["LOT"]
        event_distance = distance(target_lat, target_lon, event_lat, event_lon)
        closest_events.append((event, event_distance))
    
    # 거리를 기준으로 정렬
    closest_events.sort(key=lambda x: x[1])

    # 가장 가까운 장소 num_closest개 만큼 선택
    nearest_events = closest_events[:num_closest]

    result = []
    for event, distance in nearest_events:
        result.append(event)
    
    return result