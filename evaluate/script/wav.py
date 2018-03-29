def genWaveHeader(data) :
    length = len(data);
    header = "RIFF";
    size = 4 + 24 + 8 + length;
    ch = chr((size & 0x000000FF) >> 0);
    header += ch;    
    ch = chr((size & 0x0000FF00) >> 8);
    header += ch;    
    ch = chr((size & 0x00FF0000) >> 16);
    header += ch;    
    ch = chr((size & 0xFF000000) >> 24);
    header += ch;
    header += "WAVE";
    
    header += "fmt ";
    ch = chr((16 & 0x000000FF) >> 0);
    header += ch;    
    ch = chr((16 & 0x0000FF00) >> 8);
    header += ch;    
    ch = chr((16 & 0x00FF0000) >> 16);
    header += ch;    
    ch = chr((16 & 0xFF000000) >> 24);
    header += ch;
    
    ch = chr((1 & 0x00FF) >> 0);
    header += ch;  
    ch = chr((1 & 0xFF00) >> 8);
    header += ch;    
    
    ch = chr((1 & 0x00FF) >> 0);
    header += ch; 
    ch = chr((1 & 0xFF00) >> 8);
    header += ch;    
    
    ch = chr((16000 & 0x000000FF) >> 0);
    header += ch;
    ch = chr((16000 & 0x0000FF00) >> 8);
    header += ch;    
    ch = chr((16000 & 0x00FF0000) >> 16);
    header += ch;    
    ch = chr((16000 & 0xFF000000) >> 24);
    header += ch;
    
    ch = chr((32000 & 0x000000FF) >> 0);
    header += ch;
    ch = chr((32000 & 0x0000FF00) >> 8);
    header += ch;   
    ch = chr((32000 & 0x00FF0000) >> 16);
    header += ch;   
    ch = chr((32000 & 0xFF000000) >> 24);
    header += ch;  
     
    ch = chr((2 & 0x00FF) >> 0);
    header += ch;
    ch = chr((2 & 0xFF00) >> 8);
    header += ch;   
    
    ch = chr((16 & 0x00FF) >> 0);
    header += ch;    
    ch = chr((16 & 0xFF00) >> 8);
    header += ch;    
    
    header += "data";   
    ch = chr((length & 0x000000FF) >> 0);
    header += ch;  
    ch = chr((length & 0x0000FF00) >> 8);
    header += ch; 
    ch = chr((length & 0x00FF0000) >> 16);
    header += ch;  
    ch = chr((length & 0xFF000000) >> 24);
    header += ch;
    
    return bytearray(header, "latin1");