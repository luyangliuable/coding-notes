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
  $name = $json_a[0]['name'];
  $id = $json_a[0]['id'];
  
  if (isset($_POST["favourite"]) && !empty($_POST["favourite"]) &&
      isset($_POST["order"]) && !empty($_POST["order"]) ) 
  {

    	 //check POST information to update reference
	  $sql1 = "select PreferenceID,favourite from preference where Owner=$id";
	   if (!$result = $conn->query($sql1)) {
		echo "</div>";
		echo "</nav>";
		echo "<div class='container text-center'>";
		die('There was an error running the query [' . $conn->error . ']\n');
		echo "</div>";
	    }
	/* convert the select return result into array type */
	   $return_arr1 = array();
	   while($row = $result->fetch_assoc()){
		array_push($return_arr1,$row);
	   }
	/* convert the array type to json format and read out*/
	    $json_str = json_encode($return_arr1);
	    $json_a = json_decode($json_str,true);
	    $prefid = $json_a[0]['PreferenceID'];
    	
	$newfavourite = $_POST["favourite"] . " ";
    	$newfavourite.= $_POST["order"];

	/*check insert or update prefid*/
	if($prefid!=""){      
     		$sql2 = "UPDATE preference SET favourite='$newfavourite' where PreferenceID=$prefid;";
  	}else{
  		$sql2 = "INSERT INTO preference(favourite,Owner) VALUES ('$newfavourite', $id);";
	}

 	if (!$result = $conn->query($sql2)) {
		echo "</div>";
		echo "</nav>";
		echo "<div class='container text-center'>";
		die('There was an error running the query [' . $conn->error . ']\n');
		echo "</div>";
	}else{
	  	$conn->close();
	  	header("Location: unsafe_tasks_view.php");
	  	exit();
       }

     }
  ?>

  <div class="container  col-lg-6 col-lg-offset-4 text-center" style="padding-top: 50px; text-align: center;">
    <?php
    session_start();
    $name=$_SESSION["name"];
    echo "<h2><b>$name's Task Sort Order Preference</b></h1><hr><br>";
    ?>
    <form action="" id="form1" name="form1" method="POST" onsubmit="return validate();">
      <div class="form-group row">
        <label for="favourite" class="col-sm-4 col-form-label">What info do you prefer to sort?</label>
        <div class="col-sm-8">
	  <select id="favourite" name="favourite" >
			  <option value="Name" >Name</option>
			  <option value="Hours" selected>Hours</option>
			  <option value="Amount">Amount</option>
			  <option value="Description">Description</option>
			  <option value="Type">Type</option>
	   </select>
         </div>
      </div>
      <div class="form-group row">
        <label for="order" class="col-sm-4 col-form-label">Asc or Desc</label>
        <div class="col-sm-8">
          <input type="text" class="form-control" id="order" name="order" placeholder="asc or desc" value="asc">
        </div>
      </div>
  
      <div class="form-group row">
        <div class="col-sm-12">
          <button type="submit" class="btn btn-success btn-lg btn-block">Update</button>
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
	   var e         =  document.getElementById("favourite");
	   var favourite = e.options[e.selectedIndex].value;
	   var order            = document.form1.order.value ;

	  if(favourite=="" || order=="") 
	    {       
		 alert("Sort preference must be not empty");    
		 document.form1.order.value="";
		 document.form1.order.focus();
		 return false ;
	    }
  }
   

  </script>
</body>
</html>
