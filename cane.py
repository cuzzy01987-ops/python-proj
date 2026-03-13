import math
def main():
    name = ["#1Picnic", "#1 Tall ", "#2", "#2.5", "#3 cylinder",
            "#5", "#6Z", "8Z short",
            "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32,10.79,  13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.59, 11.91, 11.91, 14.29, 10.16, 10.16, 17.78, 12.70, 11.43, 11.43]
    cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    
    
    
    
    
    for i in range(len(name)):
        eff = efficiency(radius[i], height[i])
        cost_per = cost_per_can(radius[i], height[i], cost[i])
        print(f"{name[i]}: {eff:.2f}")
        
  
   

def cost_per_can(radius, height, cost_eff):
    volume = volume_of_cane(radius, height)
    cost = volume / cost_eff
    return cost
def efficiency(radius, height):
    volume = volume_of_cane(radius, height)
    area = surface_area(radius,height)
    eff = storage_efficiency(volume, area)
    return eff
def storage_efficiency(volume_cane, surface_area):
    storage_eff = volume_cane / surface_area
    return storage_eff
def surface_area(radius,height):
    surface_area = 2*math.pi * radius *(radius + height) 
    return surface_area
def volume_of_cane(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume


main()