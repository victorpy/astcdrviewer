<?php
// Conectando, seleccionando la base de datos
$conn = mysql_connect('localhost', 'root', 'password')
    or die('No se pudo conectar: ' . mysql_error());
echo 'Connected successfully';
mysql_select_db('asteriskcdrdb') or die('Cannot select DB');

$query = "SELECT * FROM cdrtmp where  israted = 0 and disposition = 'ANSWERED' AND accountcode != ''";
$result = mysql_query($query) or die('Query Error: ' . mysql_error());

//extract cdr from answered calls
while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
    //echo "\n";
    #echo "row: ".$row['dst']."\n";
    $accountcode = $row['accountcode'];
    $cdrdst = $row['dst'];
    $billsec = $row['billsec'];

    //search in account prefix and rate group
    $tmpqry1 = "SELECT prefix, id_rate_group,extension FROM accounts WHERE account_code=".$row['accountcode'];

    $rst_tmpqry1 = mysql_query($tmpqry1) or die('Query Error: ' . mysql_error());

    if(mysql_num_rows($rst_tmpqry1)== 0){
       echo "rsttmpqry1 no account found for ".$row['accountcode']."\n";
	continue;
    }

    $row_rsttmpqry1= mysql_fetch_array($rst_tmpqry1, MYSQL_ASSOC);

    $prefix = $row_rsttmpqry1['prefix'];
    $extension = $row_rsttmpqry1['extension'];

    //find rates with rate_group
    $ratesqry = "SELECT * FROM rate WHERE id_rate_group=".$row_rsttmpqry1['id_rate_group']." ORDER BY destination DESC" ;

    $rst_ratesqry = mysql_query($ratesqry) or die('Query Error: ' . mysql_error());
    
    if(mysql_num_rows($rst_ratesqry)== 0){
       echo "rst_ratesqry no rate found for ".$row['accountcode']."\n";
        break;
    }
     
    //search rate for cdr dst
    //remove prefix
    $cdrdst = substr_replace($cdrdst, "", 0, strlen($prefix));

    $ratefound = 0;

    while($raterow = mysql_fetch_array($rst_ratesqry, MYSQL_ASSOC)){

        $ratedst = $raterow['destination'];

        $tmpstr = substr($cdrdst, 0, strlen($ratedst));

        if($tmpstr == $ratedst){ 
		echo "rate found\n";
		$ratefound = 1;
		$amount1 = $raterow['amount1'];
		$amount2 = $raterow['amount2'];
		$cad1 = $raterow['cadence1'];
		$cad2 = $raterow['cadence2'];
		break;
	}
	
    }

    if($ratefound == 0){
	echo "rate not found for destination $cdrdst and accountcode $accountcode \n";
	break;
    }

    //calculate call amount
    if($billsec > $cad1){
      	$t1 = $billsec - $cad1;
      	$amount = $amount1;
      
      	if($t1 > $cad2){
		$slicest1 = ceil($t1/$cad2);
		$amount = $amount + ($slicest1 * $amount2);
	} else {
		$amount = $amount + $amount2;
	}

    } else {
	$amount = $amount1;
    }
    
	//echo "the amount is ".$amount." the time is ".$billsec."\n";

    //set cdr as rated
	$updratedqry = "UPDATE cdrtmp SET israted=1 WHERE acctid=".$row['acctid'];

	if (mysql_query($updratedqry)) {
    		echo "Record updated successfully ".$row['acctid']."\n";
	} else {
		echo "Error updating record in cdrtmp ".$row['acctid']." ".mysql_error()."\n";
	}

    //discount amount from credit

	$updcreditqry = "UPDATE accounts SET credit= credit-".$amount." WHERE account_code=".$row['accountcode'];

        if (mysql_query($updcreditqry)) {
                echo "Record updated successfully ".$row['acctid']."\n";
        } else {
                echo "Error updating record in account: ".$row['acctid']." ".mysql_error()."\n";
        }


    //insert into rated_cdr
	
	$insratedcdr = "INSERT INTO rated_cdr (calldate, clid, dst, amount, accountcode, billsec) VALUES 
		('".$row['calldate']."','".$extension."' , '".$row['dst']."' , '".$amount."', '".$row['accountcode']."', '".$row['billsec']."')";

	if (mysql_query($insratedcdr)) {
		echo "New record created successfully ".$row['acctid']."\n";
	} else {
    		echo "Error inserting record: ".$row['acctid']." ".mysql_error()."\n";
	}

    //echo "\n";
	mysql_free_result($rst_tmpqry1);
	mysql_free_result($rst_ratesqry);
}


// free result
mysql_free_result($result);

// close conn
mysql_close($conn);
?>

