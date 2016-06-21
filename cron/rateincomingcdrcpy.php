<?php
// Conectando, seleccionando la base de datos
$conn = mysql_connect('localhost', 'root', 'password')
    or die('No se pudo conectar: ' . mysql_error());
echo 'Connected successfully';
mysql_select_db('asteriskcdrdb') or die('Cannot select DB');

$query = "SELECT * FROM cdrtmp where  israted = 0 and disposition = 'ANSWERED' AND billsec >= 1";
$result = mysql_query($query) or die('Query Error: ' . mysql_error());

//incoming call discount
$incoming_rate=100;
//extract cdr from answered calls

while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
    //echo "\n";
    #echo "row: ".$row['dst']."\n";
    //$accountcode = $row['accountcode'];
    $cdrdst = $row['dst'];
    #$billsec = $row['billsec'];

    //search in account extension
    $tmpqry1 = "SELECT account_code,extension FROM accounts WHERE extension='".$row['dst']."'";

    $rst_tmpqry1 = mysql_query($tmpqry1) or die('Query Error: ' . mysql_error());

    if(mysql_num_rows($rst_tmpqry1)== 0){
       echo "rsttmpqry1 no account found for destination ".$row['dst']."\n";
	continue;
    }

    $row_rsttmpqry1= mysql_fetch_array($rst_tmpqry1, MYSQL_ASSOC);

    $accountcode = $row_rsttmpqry1['account_code'];
    $extension = $row_rsttmpqry1['extension'];

    //TODO search rate for incomming calls
    $incoming_rate=100;
    $amount = $incoming_rate;
	//echo "the amount is ".$amount." the time is ".$billsec."\n";

    //set cdr as rated
	$updratedqry = "UPDATE cdrtmp SET israted=1 WHERE acctid=".$row['acctid'];

	if (mysql_query($updratedqry)) {
    		echo "Record updated successfully ".$row['acctid']."\n";
	} else {
		echo "Error updating record in cdrtmp ".$row['acctid']." ".mysql_error()."\n";
	}

    //discount amount from credit

	$updcreditqry = "UPDATE accounts SET credit= credit-".$amount." WHERE account_code=".$accountcode;

        if (mysql_query($updcreditqry)) {
                echo "Record updated successfully ".$row['acctid']."\n";
        } else {
                echo "Error updating record in account: ".$row['acctid']." ".mysql_error()."\n";
        }


    //insert into rated_cdr
	
	$insratedcdr = "INSERT INTO rated_cdr (calldate, clid, dst, amount, accountcode, billsec) VALUES 
		('".$row['calldate']."','".$row['clid']."' , '".$row['dst']."' , '".$amount."', '".$row['accountcode']."', '".$row['billsec']."')";

	if (mysql_query($insratedcdr)) {
		echo "New record created successfully ".$row['acctid']."\n";
	} else {
    		echo "Error inserting record: ".$row['acctid']." ".mysql_error()."\n";
	}

    //echo "\n";
	mysql_free_result($rst_tmpqry1);
}


// free result
mysql_free_result($result);

// close conn
mysql_close($conn);
?>

