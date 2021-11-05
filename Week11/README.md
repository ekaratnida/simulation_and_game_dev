# Outline
## 1. Instantiate prefab at runtime. 
### Ref: https://docs.unity3d.com/Manual/InstantiatingPrefabs.html

1.1 A simple example
``` c#
using UnityEngine;
public class InstantiationExample : MonoBehaviour 
{
    // Reference to the Prefab. Drag a Prefab into this field in the Inspector.
    public GameObject myPrefab;

    // This script will simply instantiate the Prefab when the game starts.
    void Start()
    {
        // Instantiate at position (0, 0, 0) and zero rotation.
        Instantiate(myPrefab, new Vector3(0, 0, 0), Quaternion.identity);
    }
}
```

1.2 Building a structure

```c#
using UnityEngine;
public class Wall : MonoBehaviour
{
   public GameObject block;
   public int width = 10;
   public int height = 4;
  
   void Start()
   {
       for (int y=0; y<height; ++y)
       {
           for (int x=0; x<width; ++x)
           {
               Instantiate(block, new Vector3(x,y,0), Quaternion.identity);
           }
       }       
   }
}
```

1.3 More complex structures

``` c#
using UnityEngine;
public class CircleFormation : MonoBehaviour
{
   // Instantiates prefabs in a circle formation
   public GameObject prefab;
   public int numberOfObjects = 20;
   public float radius = 5f;
   void Start()
   {
       for (int i = 0; i < numberOfObjects; i++)
       {
           float angle = i * Mathf.PI * 2 / numberOfObjects;
           float x = Mathf.Cos(angle) * radius;
           float z = Mathf.Sin(angle) * radius;
           Vector3 pos = transform.position + new Vector3(x, 0, z);
           float angleDegrees = -angle*Mathf.Rad2Deg;
           Quaternion rot = Quaternion.Euler(0, angleDegrees, 0);
           Instantiate(prefab, pos, rot);
       }
   }
}
```
1.4 Fire a bullet

```
    if (Input.GetButtonDown("Fire1"))
    {
        Rigidbody p = Instantiate(projectile, transform.position, transform.rotation);
        p.velocity = transform.forward * speed;
    }
```

### Exercise
1. Fire a block. If it hits any object, connect it to that one. You can use a block to cross a high wall or as a bridge.
   Example, - [![Hitori](https://img.youtube.com/vi/Evc2zNT09gQ/0.jpg)](https://www.youtube.com/clip/UgkxqXyRfZhT7SSpT9qLCXQhuRMkPj4yjGER) 
