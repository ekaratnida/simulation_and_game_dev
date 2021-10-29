# Realtime CSG https://realtimecsg.com/#modeling-with-brushes
## Control
### Input
Mouse: https://docs.unity3d.com/ScriptReference/Input.html <br>
Press space: https://docs.unity3d.com/ScriptReference/Input.GetKeyDown.html <br>
Add force: https://docs.unity3d.com/ScriptReference/Rigidbody.AddForce.html

## 1. Player
![week10-1](https://user-images.githubusercontent.com/69342162/139366010-00096599-0e82-4963-a479-7d297bbd4f60.png)


``` c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player2 : MonoBehaviour
{
    Rigidbody m_Rigidbody;
    int speedY = 300;
    bool isTouchFloor = false; 
    // Start is called before the first frame update
    void Start()
    {
        m_Rigidbody = GetComponent<Rigidbody>();
    }

   
    // Update is called once per frame
    void Update() //FixedUpdate()
    {
        //Not allow users to press while player is in the air.
        if(Input.GetKeyUp("space") ||  Input.GetButtonUp("Fire1") && isTouchFloor){
            isTouchFloor = false;
            print("Space key was released");
            var position = new Vector3(0,speedY,0);
            m_Rigidbody.AddForce(position);
        }

    }

    void OnCollisionEnter(Collision collision)
    {
        var objName = collision.gameObject.name;
        if ( objName == "Plane")
        {
            //If the GameObject's name matches the one you suggest, output this message in the console
            Debug.Log("Do something here "+objName);
            isTouchFloor = true;
        }

        if ( objName == "ball")
        {
            m_Rigidbody.velocity = Vector3.zero;
            collision.gameObject.GetComponent<Rigidbody>().velocity = Vector3.zero;
            transform.position = new Vector3(-3.5f,1,0);
            collision.gameObject.transform.position = new Vector3(5,1,0);
        }
    }

   
}
```

## 2. Ball

![image](https://user-images.githubusercontent.com/69342162/139366596-0e0932e7-22db-4950-99b7-cc20401c75fb.png)

``` c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Ball : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    public int speedX = 0;
    public int speedZ = 0;
    int score = 0;
    // Update is called once per frame
    void Update()
    {
        var position = new Vector3(speedX,0,0);
        transform.Translate(position * Time.deltaTime);

        if(transform.position.x < -5){
            ++score;
            transform.position = new Vector3(5,1,0);
        } 
    }

    GUIStyle style = new GUIStyle();
    void OnGUI()
    {
        style.fontSize = 20; //change the font size
        GUI.Label(new Rect(10, 10, 100, 20), score.ToString(),style);
    }

    private void OnTriggerEnter(Collider other)
    {
        transform.position = new Vector3(5,1,0);
    }
}

```
## realtime csg
<font size="5"> 1. Install realtime csg: Goto menu > window > package manager > "Search realtime csg" > install </font>

<font size="5"> 2. Tutorial1: <br>
   - https://www.youtube.com/watch?v=uqaiUMuGlRc <br>
   - https://www.youtube.com/watch?v=TUkKNoIQ1bk <br> </font>

<font size="5"> 3. Exercise1: Create your own item <br> </font>

<font size="5"> 4. FPSController for testing your environment. just drag and drop <br> 
   -- Assests/Standard Assets/Characters/FirstPersonCharacter/Prefabs/FPSController.prefab <br> </font>
