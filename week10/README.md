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
![image](https://user-images.githubusercontent.com/69342162/139370817-cf675023-c68c-4ad5-a70c-265428d86880.png)
Reference: https://docs.unity3d.com/Manual/class-Rigidbody.html

## 3. Model and animation
![image](https://user-images.githubusercontent.com/69342162/139386141-45a4b339-6279-4941-a30c-c24738798d2e.png)
``` c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimController : MonoBehaviour
{

    private Animator animator;

    // Start is called before the first frame update
    void Start()
    {
       animator =  gameObject.GetComponent<Animator>();
    }

    public float speedz = 2f;
    // Update is called once per frame
    void Update()
    {
        if(Input.GetKey(KeyCode.W)){
            animator.SetBool("isWalking",true);
            transform.Translate(0,0, speedz * Time.deltaTime);
           
        } 
        else if(Input.GetKeyUp(KeyCode.W)){
            animator.SetBool("isWalking",false);
        }

         if(Input.GetKey(KeyCode.S)){
            animator.SetBool("isWalking",true);
            transform.Translate(0,0, -speedz * Time.deltaTime);
           
        } 
        else if(Input.GetKeyUp(KeyCode.S)){
            animator.SetBool("isWalking",false);
        }

        if(Input.GetKeyDown(KeyCode.Space) || Input.GetButtonDown("Fire1")){
            animator.SetBool("isJump",true);
        
        }else if(Input.GetKeyUp(KeyCode.Space) || Input.GetButtonUp("Fire1")){
            animator.SetBool("isJump",false);
        }
    }
}
```

## Exercise
1. Deduct your score if hit the ball.
2. What is trigger? Why not assigned rigidbody component to the ball?
3. Add a new gameplay
4. Change the player and ball to model & animatios.

Animation tutorial
[![Animation](https://img.youtube.com/vi/UOb6IK43cJQ/0.jpg)](https://www.youtube.com/watch?v=UOb6IK43cJQ)


## realtime csg
<font size="5"> 1. Install realtime csg: Goto menu > window > package manager > "Search realtime csg" > install </font>

<font size="5"> 2. Tutorial1: <br>
   - https://www.youtube.com/watch?v=uqaiUMuGlRc <br>
   - https://www.youtube.com/watch?v=TUkKNoIQ1bk <br> </font>

<font size="5"> 3. Exercise1: Create your own item <br> </font>

<font size="5"> 4. FPSController for testing your environment. just drag and drop <br> 
   -- Assests/Standard Assets/Characters/FirstPersonCharacter/Prefabs/FPSController.prefab <br> </font>
