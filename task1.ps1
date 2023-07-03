

# works sometimes? 
$infile = Import-CSV "C:\Users\sierrapine\IN-task1\test2.csv"

foreach ($line in $infile)
#foreach $line in $file
{
    $compname = $line.Name
    $results = Test-NetConnection -Computername $compname -Port 5985 -InformationLevel Quiet 

    #Write-Host $compname
    if ($results.TcpTestSucceeded)
    {
        Write-Host "Port is open for $compname"
    }
    else
    {   
        Write-Host "Port is closed for $compname"
    }
    
}





<#
 $ipaddress = $line.Data
    $port = 5986
    $connection = New-Object System.Net.Sockets.TcpClient($ipaddress, $port)
    
    if ($connection.Connected) {
        Write-Host "Success" 
    } 
    else { 
        Write-Host "Failed" 
    }
#>

   
