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

  <div  margin-bottom: 1px; class="container  col-lg-8 col-lg-offset-4 text-center" style="padding-top: 5px; text-align: center;">
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

    
    $name=$_SESSION["name"];
    echo "<h2><b>$name's Declared Tasks</b></h1><hr><br>";
    ?>
    <br>
  </div>
 
	  <?php
	  session_start();
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

	  /* retrieve favourite preference first*/
	  $sql = "select favourite from preference where owner=$id limit 1";
	  if (!$result = $conn->query($sql)) {
	    echo $sql;
	    die('There was an error running the query [' . $conn->error . ']\n');
	  }
 	 
	  $return_arr = array();
	  while($row = $result->fetch_assoc()){
	    array_push($return_arr,$row);
	  }
	  $json_str = json_encode($return_arr);
	  $json_a = json_decode($json_str,true);
	  $favourite = $json_a[0]['favourite'];
	  if($favourite==""){
		$favourite = "hours desc";
	  }     

	  
	  /*construct task query statement*/
	  $sql1 = "select tasks.Name as taskname, credential.Name as ownername, tasks.Hours,tasks.Amount,tasks.Description,tasks.Type from tasks, credential where tasks.owner=credential.ID and tasks.owner=$id " . "order by tasks." . $favourite ;
	  
	  //split by ";" if this is a batch queries
	  $queryList = explode(";",$sql1);

	  $displayResult ="";

	  foreach($queryList as $subquery){
	     //echo $subquery;
	     if(strlen($subquery)>0) {
	     
		    //batch queries multiple returns result append- check length of row if is not 5 then just append to another textarea
		    if (!$tempResult = $conn->query($subquery)) {
		    	die('There was an error running the query [' . $conn->error . ']\n');
			$conn->close();
			exit();
		    }

		    //convert from json obj to Php array
		    $return_arr = array();
		    while($row = $tempResult->fetch_assoc()){
		    	array_push($return_arr,$row);
		    }
		    $json_str = json_encode($return_arr);
		    $json_a = json_decode($json_str,true);
		    
		    
			    $newTable = "<div class='container col-lg-4 col-lg-offset-4'>";
			    $newTable .= "<table border='3' align='center' style='text-align:left'>";
			    $newTable .= "<tr><td>Task Name</td><td>Task Owner</td><td>Hours</td><td>Amount</td><td>Task Description</td><td>Type</td></tr>";
			    //render each element to a Table Row
			    foreach($json_a as $newItem){
			   	$newRow="<tr>";
				foreach($newItem as $val ) $newRow.="<td>$val</td>";
				$newRow.="<tr>";

				$newTable.=$newRow;
			    }

			    $newTable.="</table>";
			    $newTable.= "</div>";
			    echo $newTable;
			    //$displayResult.=$newTable;
		
		    echo "<br><br>";
		   // $displayResult.= "<br><br>";
	    }
	}
	
	 //echo $displayResult;
	 
	  ?>



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
  </script>
</body>
</html>
