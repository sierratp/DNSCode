

$infile = Import-CSV "C:\Users\sierrapine\IN-task1\test3.csv"

$timeoutMilliseconds = 2000

foreach ($line in $infile)
{
    $compname = $line.Name
    $tcpClient = New-Object System.Net.Sockets.TcpClient

    # Set the timeout value for the TCP client
    $tcpClient.ReceiveTimeout = $timeoutMilliseconds

    try {
        $tcpClient.Connect($compname, 5986)
        Write-Host "Port is open for $compname"
    }
    catch {
        Write-Host "Port is closed for $compname"
    }
    
    # Close the TCP client connection
    $tcpClient.Close()
}

