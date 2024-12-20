/*
 * Copyright (C) 2017 Texas Instruments Incorporated - http://www.ti.com/
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the
 * distribution.
 *
 * Neither the name of Texas Instruments Incorporated nor the names of
 * its contributors may be used to endorse or promote products derived
 * from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
/**
 *  \file   app.h
 *
 *  \brief  Template application header file
 */


/* Standard header files */
#include <string.h>

/* XDCtools Header files */
#include <xdc/std.h>
#include <xdc/cfg/global.h>
#include <xdc/runtime/System.h>
#include <xdc/runtime/Error.h>

/* BIOS Header files */
#include <ti/sysbios/BIOS.h>
#include <ti/sysbios/knl/Task.h>

/* Modification: Add the Mailbox header file */
#include <ti/sysbios/knl/Mailbox.h>

/* Low level driver header files */
#include <ti/drv/gpio/GPIO.h>
#include <ti/drv/uart/src/UART_utils_defs.h>
#include <ti/drv/uart/UART_stdio.h>
#include <ti/drv/uart/UART.h>
#include <ti/drv/i2c/I2C.h>
#include <ti/drv/spi/MCSPI.h>

/* Board header file */
#include <ti/board/board.h>

/* Local GPIO board header file */
#include "GPIO_board.h"

/**********************************************************************
 ************************** Macros ************************************
 **********************************************************************/
/* Route all application prints to UART */
#define appPrint                UART_printf

/**
 *  @brief Function appTasksCreate : Creates multiple application tasks
 *
 *  @param[in]         None
 *  @retval            none
 */
void appTasksCreate(void);

/* External functions */
extern void GPIOApp_UpdateBoardInfo(void);

/**********************************************************************
 ************************** Application parameters ********************
 **********************************************************************/
/* LED Blink Delay value */
#define LED_BLINK_DELAY_VALUE       (1000)
/* Decide LED GPIO index : Refer to GPIO_PinConfig structure to see
 * which LED is assigned to the respective GPIO index */
#define TEST_LED_GPIO_INDEX GPIO_USER_LED1
