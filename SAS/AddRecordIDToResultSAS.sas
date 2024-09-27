/* Using DS2 to create a RecordID, which is useful when dealing with data */
%LET number = 0;
PROC DS2;
DATA result /OVERWRITE = YES;
    DCL INT RecordID;
    METHOD init();
    RecordID = %TSLIT(&number);
    END;
        /*GLOWNA*/
        METHOD run();
        SET query_result;
        RecordID + 1;
        END;
    /*NA KONIEC*/
    METHOD term();
    PUT 'Koniec !!!';
    END;
ENDDATA;
RUN;
QUIT;
PROC PRINT
    DATA = work.result;
RUN;