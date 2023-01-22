<!--
SEED Lab: SQL Injection Education Web plateform
Author: Viet Vo
Email: viet.vo@monash.edu
-->

<html>
<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link href="css/style_home.css" type="text/css" rel="stylesheet">

  <!-- Browser Tab title -->
  <title>SQLi Lab</title>
</head>

<body>
  <nav class="navbar fixed-top navbar-expand-lg navbar-light" style="background-color: #3EA055;">
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <a class="navbar-brand" href="unsafe_home.php" ><img src="seed_logo.png" style="height: 40px; width: 200px;" alt="SEEDLabs"></a>
      <ul class='navbar-nav mr-auto mt-2 mt-lg-0' style='padding-left: 30px;'>
        <li class='nav-item'>
          <a class='nav-link' href='unsafe_home.php'>Home</a>
        </li>
        <li class='nav-item active'>
          <a class='nav-link' href='unsafe_edit_frontend.php'>Edit Profile</a>
        </li>
        <li class='nav-item active'>
          <a class='nav-link' href='unsafe_task_load.php'>Add Task</a>
        </li>
        <li class='nav-item active'>
          <a class='nav-link' href='unsafe_view_order.php'>Set View Preference</a>
        </li>
        <li class='nav-item active'>
          <a class='nav-link' href='unsafe_tasks_view.php'>View Tasks</a>
        </li>
      </ul>
      <button onclick='logout()' type='button' id='logoffBtn' class='nav-link my-2 my-lg-0'>Logout</button>
    </div>
  </nav>

  <?php

	 session_start();
    
    //auto log out after 20 mins 
	function auto_logout($field)
	{
	    $t = time();
	    $t0 = $_SESSION[$field];
	    $diff = $t - $t0;
	    if ($diff > 1200 || !isset($t0))
	    {          
		return true;
	    }
	    else
	    {
		$_SESSION[$field] = time();
	    }
	}
	
       if(auto_logout("user_time"))
       {
		session_unset();
		session_destroy();
		location("index.html");          
		exit;
    	}


 
  $uname = $_SESSION['name'];
  

  // Function to create a sql connection.
  function getDB() {
    $dbhost="localhost";
    $dbuser="root";
    $dbpass="seedubuntu";
    $dbname="Users";
    // Create a DB connection
    $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error . "\n");
    }
    return $conn;
  }

  // create a connection
  $conn = getDB();
  // Sql query to authenticate the user
  $sql = "SELECT id, name, eid, salary, birth, ssn, phoneNumber, address, email,nickname,Password
  FROM credential
  WHERE name= '$uname'";
  if (!$result = $conn->query($sql)) {
    die('There was an error running the query [' . $conn->error . ']\n');
  }
  /* convert the select return result into array type */
  $return_arr = array();
  while($row = $result->fetch_assoc()){
    array_push($return_arr,$row);
  }

  /* convert the array type to json format and read out*/
  $json_str = json_encode($return_arr);
  $json_a = json_decode($json_str,true);
  $id = $json_a[0]['id'];
  $name = $json_a[0]['name'];
  
  //check POST information to add a new task
  if (isset($_POST["Name"]) && !empty($_POST["Name"]) &&
      isset($_POST["Hours"]) && !empty($_POST["Hours"]) &&
      isset($_POST["Amount"]) && !empty($_POST["Amount"]) &&
      isset($_POST["Description"]) && !empty($_POST["Description"]) &&
      isset($_POST["Type"]) && !empty($_POST["Type"]))
  {
    
        $taskname = $_POST["Name"];
 	$taskhours = $_POST["Hours"];
	$taskamount = $_POST["Amount"];
	$taskdescription = $_POST["Description"];
	$tasktype = $_POST["Type"];

	    // Sql query to insert a new task of  the current user
	  $sql1 = "INSERT INTO tasks (Name, Hours, Amount, Description,Owner,Type) VALUES ('$taskname',$taskhours,$taskamount,'$taskdescription',$id,'$tasktype')";
        
   if (!$result = $conn->query($sql1)) {
    die('There was an error running the query [' . $conn->error . ']\n');
	$conn->close();
   } else
   {
      $conn->close();
     header("Location: unsafe_tasks_view.php");
     exit();
   }

  }

  ?>

  <div  margin-bottom: 1px; class="container  col-lg-8 col-lg-offset-4 text-center" style="padding-top: 5px; text-align: center;">
    <?php
    session_start();
    $name=$_SESSION["name"];
    echo "<h2><b>$name's Task Declaration</b></h1><hr><br>";
    ?>
    <form action="" id="form1" name="form1" method="POST" onsubmit="return validate();">
      <div class="form-group row">
        <label for="Name" class="col-sm-4 col-form-label">Name</label>
        <div class="col-sm-8">
          <input type="text" class="form-control" id="Name" name="Name" placeholder="Task Name">
        </div>
      </div>
      <div class="form-group row">
        <label for="Hours" class="col-sm-4 col-form-label">Hours</label>
        <div class="col-sm-8">
          <input type="text" class="form-control" id="Hours" name="Hours" placeholder="Hours required">
        </div>
      </div>
      <div class="form-group row">
        <label for="Amount" class="col-sm-4 col-form-label">Amount</label>
        <div class="col-sm-8">
          <input type="text" class="form-control" id="Amount" name="Amount" placeholder="Amount required">
        </div>
      </div>
      <div class="form-group row">
        <label for="Description" class="col-sm-4 col-form-label">Description</label>
        <div class="col-sm-8">
          <input type="text" class="form-control" id="Description" name="Description" placeholder="Task Description">
        </div>
      </div>
      <div class="form-group row">
        <label for="Type" class="col-sm-4 col-form-label">Type</label>
        <div class="col-sm-8">
          <input type="text" class="form-control" id="Type" name="Type" placeholder="Collaborative or Individual">
        </div>
      </div>
      <br>
      <div class="form-group row">
        <div class="col-sm-12">
          <button type="submit" class="btn btn-success btn-lg btn-block">Add</button>
        </div>
      </div>
    </form>
    <br>
   
  </div>

      <br><br>
      <div class="text-center">
        <p>
          FIT3173 Software Security
        </p>
      </div>
    </div>

  <script type="text/javascript">
  function logout(){
    location.href = "logoff.php";
  }

  function validate(){
	
    var numbercheck   =/^\d+$/;
    var name             = document.form1.Name.value ;
    var hours            = document.form1.Hours.value ;
    var amount         = document.form1.Amount.value ;
    var description     = document.form1.Description.value ;
    var tasktype        = document.form1.Type.value ;

   if(name=="") 
    {       
         alert("Input Name");    
         document.form1.Name.value="";
         document.form1.Name.focus();
         return false ;
    }
    if(numbercheck.test(hours)==false) 
    {       
         alert("Hours must be an integer number");    
         document.form1.Hours.value="";
         document.form1.Hours.focus();
         return false ;
    }
   if(numbercheck.test(amount)==false) 
    {       
         alert("Amount must be an integer number");    
         document.form1.Amount.value="";
         document.form1.Amount.focus();
         return false ;
    }
   if(description=="") 
    {       
         alert("Input Task Description");    
         document.form1.Description.value="";
         document.form1.Description.focus();
         return false ;
    }

   if(tasktype=="") 
    {       
         alert("Input Task Type");    
         document.form1.Type.value="";
         document.form1.Type.focus();
         return false ;
    }

   }
  </script>
</body>
</html>
